import json
import torch
from torchvision import transforms, models
from PIL import Image
import io

class_labels = json.load(open('ml/cars_meta.json'))

# Model initalization
model = models.mobilenet_v3_large(weights=models.MobileNet_V3_Large_Weights.DEFAULT)
n_ftrs = model.classifier[3].in_features
n_class = len(class_labels)
model.classifier[3] = torch.nn.Linear(n_ftrs, n_class)

# Load trained model weights
state_dict = torch.load('ml/mobilenet_v3_l/weights.pt', map_location='cpu')
model.load_state_dict(state_dict)

model.eval()

def get_transform(image):
    transform = transforms.Compose([
        transforms.Resize((240, 360)),
        transforms.ToTensor(),
        transforms.Normalize((0.485, 0.456, 0.406), (0.229, 0.224, 0.225))
    ])

    return transform(image).unsqueeze(0)

def get_inference(input):
    with torch.no_grad():
        output = model(input)
        _, pred = torch.max(output, 1)

    return pred.item()

def inference(image):
    image = image.read()
    image = Image.open(io.BytesIO(image))
    image_tensor = get_transform(image)
    label_pred = get_inference(image_tensor)
    class_name = class_labels[str(label_pred)]

    return {'label': label_pred, 'class_name': class_name}