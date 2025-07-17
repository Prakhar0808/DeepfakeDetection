from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser
import numpy as np
from PIL import Image
import io

class DeepfakeDetection(APIView):
    parser_classes = [MultiPartParser]

    def post(self, request):
        uploaded_file = request.FILES.get('file')
        if not uploaded_file:
            return Response({'error': 'No file uploaded'}, status=400)

        image = Image.open(uploaded_file).resize((224, 224))
        image = np.array(image) / 255.0
        image = np.expand_dims(image, axis=0)

        # dummy prediction
        prediction = 0.87  # Replace with model.predict(image)

        return Response({'fake_probability': prediction})
