import os
import io
from flask import Flask, request, jsonify, render_template
from transformers import AutoModelForImageClassification, AutoImageProcessor
from PIL import Image
import torch
from prometheus_flask_exporter import PrometheusMetrics
from nutrition_data import get_nutrition

app = Flask(__name__)
metrics = PrometheusMetrics(app)

print("🔄 Loading food classification model...")
MODEL_NAME = "nateraw/food"
processor = AutoImageProcessor.from_pretrained(MODEL_NAME)
model = AutoModelForImageClassification.from_pretrained(MODEL_NAME)
model.eval()
print("✅ Model loaded!")

@app.route("/")
def index():
    pod_name = os.environ.get("POD_NAME", "local-dev")
    return render_template("index.html", pod_name=pod_name)

@app.route("/predict", methods=["POST"])
def predict():
    if "file" not in request.files:
        return jsonify({"error": "No file uploaded"}), 400

    file = request.files["file"]
    image = Image.open(io.BytesIO(file.read())).convert("RGB")
    inputs = processor(images=image, return_tensors="pt")

    with torch.no_grad():
        outputs = model(**inputs)
        logits = outputs.logits

    probs = torch.nn.functional.softmax(logits, dim=-1)[0]
    top3 = torch.topk(probs, 3).indices.tolist()

    results = []
    for idx in top3:
        food_name = model.config.id2label[idx]
        confidence = f"{probs[idx].item() * 100:.1f}%"
        nutrition = get_nutrition(food_name)
        results.append({
            "food": food_name.replace("_", " ").title(),
            "confidence": confidence,
            "nutrition": nutrition
        })

    return jsonify({
        "pod_name": os.environ.get("POD_NAME", "local-dev"),
        "results": results
    })

@app.route("/health")
def health():
    return jsonify({"status": "healthy"}), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)