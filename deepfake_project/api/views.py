from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser
from transformers import AutoImageProcessor, AutoModelForImageClassification
from PIL import Image
import torch

# Load once at the top
model_name = "prithivMLmods/deepfake-detector-model-v1"
processor = AutoImageProcessor.from_pretrained(model_name)
model = AutoModelForImageClassification.from_pretrained(model_name)

# Map index to labels
id2label = {
    "0": "fake",
    "1": "real"
}

class DeepfakeDetection(APIView):
    parser_classes = [MultiPartParser]

    def post(self, request):
        uploaded_file = request.FILES.get('file') or request.FILES.get('video')
        if not uploaded_file:
            return Response({'error': 'No file uploaded'}, status=400)

        try:
            # Convert to PIL Image
            image = Image.open(uploaded_file).convert("RGB")

            # Preprocess
            inputs = processor(images=image, return_tensors="pt")

            # Predict
            with torch.no_grad():
                outputs = model(**inputs)
                logits = outputs.logits
                probs = torch.nn.functional.softmax(logits, dim=1).squeeze()

            predictions = {
                id2label[str(i)]: round(probs[i].item(), 3) for i in range(len(probs))
            }

            return Response({
                "fake_probability": predictions.get("fake", 0.0),
                "predictions": predictions
            })

        except Exception as e:
            return Response({'error': str(e)}, status=500)
