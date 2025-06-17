from flask import Flask, render_template, Response
import cv2
from ultralytics import YOLO
app = Flask(__name__, template_folder="../frontend/templates")
model = YOLO("yl1.pt")
model.model.names = {           #ghi đè tên các lớp do lỗi font chữ,thứ tự
    0: "Bia Cung",
    1: "Thuy Tinh",
    2: "Kim Loai",
    3: "",
    4: "Cac loai khac",
    5: "Nhua",
    6: "Giay",
    7: "Xop",
}
camera = cv2.VideoCapture(0)
def gen_frames():
    while True:
        success, frame = camera.read()
        if not success:
            break
        # Nhận diện
        results = model(frame, stream=True)
        # Vẽ khung quanh rác
        for r in results:
            for box in r.boxes:
                x1, y1, x2, y2 = map(int, box.xyxy[0])
                conf = box.conf[0]
                cls = int(box.cls[0])
                label = model.names[cls]
                cv2.rectangle(frame, (x1, y1), (x2, y2), (0,255,0), 2)
                cv2.putText(frame, f'{label} {conf:.2f}', (x1, y1 - 10),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0,255,0), 2)
        # Encode thành JPEG
        ret, buffer = cv2.imencode('.jpg', frame)
        frame = buffer.tobytes()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')
@app.route('/')
def index():
    return render_template('index.html')
@app.route('/video_feed')
def video_feed():
    return Response(gen_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=1503)
