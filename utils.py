import torch
import torchvision.models as models
from torchvision import transforms
from PIL import Image
import torch.nn.functional as F
import streamlit as st
import utils

# Daftar kelas
class_labels = [
    'FreshApple', 'FreshBanana', 'FreshMango', 'FreshOrange', 'FreshStrawberry',
    'RottenApple', 'RottenBanana', 'RottenMango', 'RottenOrange', 'RottenStrawberry'
]

# Fungsi untuk memuat model dengan caching
@st.cache_resource
def load_model():
    num_classes = len(class_labels)
    model = models.resnet50(pretrained=False)
    num_ftrs = model.fc.in_features
    model.fc = torch.nn.Linear(num_ftrs, num_classes)
    state_dict = torch.load('./trained_fruit_quality_modelv5.pth', map_location=torch.device('cpu'))
    model.load_state_dict(state_dict)
    model.eval()
    return model

# Fungsi prediksi kesegaran buah untuk beberapa gambar
def predict_freshness(image):
    model = load_model()
    transform = transforms.Compose([
        transforms.Resize((224, 224)),
        transforms.ToTensor(),
        transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])
    ])

    img = transform(Image.open(image).convert("RGB")).unsqueeze(0)
    with torch.no_grad():
        outputs = model(img)
        probabilities = F.softmax(outputs, dim=1)
        confidence, predicted_class = torch.max(probabilities, 1)
        confidence = confidence.item() * 100
        predicted_class = predicted_class.item()
        label = class_labels[predicted_class]
    
    if "Fresh" in label:
        freshness_percentage = probabilities[0, predicted_class].item() * 100
    else:
        freshness_percentage = (1 - probabilities[0, predicted_class].item()) * 100
    
    fruit_type = label.replace("Fresh", "").replace("Rotten", "")
    return freshness_percentage, fruit_type

# Fungsi rekomendasi untuk konsumen
def get_consumer_recommendations(freshness, fruit_type):
    # Prediksi Waktu konsumsi berdasarkan freshness
    if freshness >= 80:
        consumption_time = "8-10 jam"
    elif freshness >= 60:
        consumption_time = "6-8 jam"
    elif freshness >= 40:
        consumption_time = "4-6 jam"
    elif freshness >= 20:
        consumption_time = "2-4 jam"
    else:
        consumption_time = "0-2 jam"

    # Prediksi Waktu penyimpanan hingga busuk
    if freshness >= 80:
        storage_time = "48-72 jam"
    elif freshness >= 60:
        storage_time = "24-48 jam"
    elif freshness >= 40:
        storage_time = "12-24 jam"
    elif freshness >= 20:
        storage_time = "6-12 jam"
    else:
        storage_time = "0-6 jam"

    # Rekomendasi tempat penyimpanan berdasarkan jenis dan freshness
    if "Apple" in fruit_type or "Banana" in fruit_type:
        storage_recommendation = "Lemari es"
    elif "Mango" in fruit_type or "Orange" in fruit_type:
        storage_recommendation = "Ruangan dengan suhu dingin"
    elif "Strawberry" in fruit_type:
        storage_recommendation = "Kulkas dengan suhu rendah"
    else:
        storage_recommendation = "Tempat sejuk dan kering"

    return consumption_time, storage_time, storage_recommendation

# Fungsi rekomendasi untuk petani
def get_farmer_recommendations(freshness, fruit_type):
    # Prediksi waktu distribusi berdasarkan freshness
    if freshness >= 80:
        distribution_time = "10-12 jam"
    elif freshness >= 60:
        distribution_time = "8-10 jam"
    elif freshness >= 40:
        distribution_time = "6-8 jam"
    elif freshness >= 20:
        distribution_time = "4-6 jam"
    else:
        distribution_time = "0-4 jam"

    # Rekomendasi tempat & suhu penyimpanan selama pengiriman
    if "Apple" in fruit_type or "Banana" in fruit_type:
        storage_suggestion = "10°C - 12°C"
    elif "Mango" in fruit_type or "Orange" in fruit_type:
        storage_suggestion = "5°C - 8°C"
    elif "Strawberry" in fruit_type:
        storage_suggestion = "2°C - 4°C"
    else:
        storage_suggestion = "Suhu sejuk dan stabil"

    # Prediksi waktu pengiriman maksimal dalam hari
    if freshness >= 80:
        max_delivery_time = "5 hari"
    elif freshness >= 60:
        max_delivery_time = "4 hari"
    elif freshness >= 40:
        max_delivery_time = "3 hari"
    elif freshness >= 20:
        max_delivery_time = "2 hari"
    else:
        max_delivery_time = "Tidak Layak untuk dikirim"

    return distribution_time, storage_suggestion, max_delivery_time
