from roboflow import Roboflow

print("📥 Descargando dataset desde Roboflow...")
rf = Roboflow(api_key="1dLowTzQ1FvgIrWcjJT5")
project = rf.workspace("alejandrospace").project("object_detector_yolo11_final")
version = project.version(1)
dataset = version.download("yolov11")

from ultralytics import YOLO

print("📦 Cargando modelo base YOLOv11 (yolo11s.pt)...")
model = YOLO("yolo11s.pt")

data_path = "object_detector_yolo11_final-1/data.yaml"

print("🚀 Iniciando entrenamiento...")
results = model.train(data=data_path, epochs=50, imgsz=640)
print("✅ Entrenamiento finalizado.")

print("📊 Evaluando modelo en conjunto de validación...")
metrics = model.val()
print(f"📈 mAP@0.5: {metrics.box.map50:.4f}")

print("🔍 Cargando modelo entrenado (best.pt)...")
custom_model = YOLO("runs/detect/train/weights/best.pt")

print("📸 Realizando predicciones sobre imágenes de prueba...")
results = custom_model("object_detector_yolo11_final-1/test/images")

# Mostrar una detección específica
index = 0  # cambia este índice para ver otras imágenes
print(f"🖼 Mostrando resultado {index}...")
results[index].show()