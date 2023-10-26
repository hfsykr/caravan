# Caravan

## Install Requirements

````console
pip install -r requirements.txt
````

## Model

You can download the model weights [here](https://github.com/hfsykr/cars-classification/blob/main/output/mobilenet_v3_l/weights.pt) and move it to 'ml/mobilenet_v3_l' folder [(here)](ml/mobilenet_v3_l).

## Local/Development Run

````console
gunicorn --bind 127.0.0.1 wsgi:app
````