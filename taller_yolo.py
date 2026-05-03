import cv2
from ultralytics import YOLO

# Cargar modelo
model = YOLO('best.pt')

# Abrir cámara
cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

if not cap.isOpened():
    print("Error al abrir la cámara")
    exit()

print("Presiona 'q' para salir.")

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Realizar inferencia en el frame actual
    results = model(frame, verbose=False)
    annotated_frame = results[0].plot()

    cv2.imshow('Detección en tiempo real', annotated_frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()