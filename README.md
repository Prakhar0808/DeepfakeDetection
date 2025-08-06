🛡️ Deepfake Detection App – Syntax Squad
An AI-powered cybersecurity tool to identify manipulated content across images, videos, and audio in real-time. Designed for digital trust, this application helps fight misinformation, identity theft, and media tampering.

🔍 Overview
Deepfakes pose serious threats in the digital era—ranging from fake news to interview fraud. Our platform provides a robust detection system capable of verifying:

Manipulated faces in images and videos

Tampered audio

Fake or altered visual media

💡 Key Features
🖥️ Input Methods: Upload via web interface, use your webcam, or detect via Chrome extension

🧠 AI Models: Pretrained EfficientNetB2 and Hugging Face image/audio classifiers

⚙️ Backend: Django REST API

🌐 Frontend: React.js SPA

📦 Integration: REST API ready for job portals, proctoring tools, or content platforms

🧪 Results: Confidence scores, and optional Grad-CAM visual explanations

📊 Scalable: Future support for metadata analysis, anomaly detection, and bulk scanning

📚 Datasets Used
FaceForensics++

DeepFake Detection Challenge (DFDC)

Celeb-DF

🚀 Future Scope
Real-time deepfake detection for live streams

Audio deepfake detection using voice biometrics

Browser extensions with on-page video verification

Commercial API licensing for media platforms

Integration into job/interview portals and news verifiers

💰 Monetization – Freemium Model
-We plan to offer a Freemium Pricing Structure:

| Tier          | Features                                                                  |
| ------------- | ------------------------------------------------------------------------- |
| 🆓 Free       | - Limited daily scans<br> - Web app access<br> - Confidence score only    |
| 💼 Pro        | - Unlimited scans<br> - Full Grad-CAM visual insights<br> - Batch uploads |
| 🧩 Enterprise | - Custom API access<br> - Priority support<br> - Integration help         |


📦 Installation
Requirements

-"Python 3.8+"

-"Node.js 14+"

-"pip, npm, virtualenv"

Backend

<pre><code>```bash cd backend python -m venv venv source venv/bin/activate # or venv\Scripts\activate on Windows pip install -r requirements.txt python manage.py runserver ``` </code></pre>

Frontend
<pre><code>```bash cd frontend npm install npm start ``` </code></pre>

🧩 Demo
Add a link here after deployment or attach a demo video
Example: https://deepfakedetector-demo.vercel.app

🤝 Contributing
Pull requests are welcome! For major changes, please open an issue first to discuss.

