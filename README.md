# YOLO11 để nhận diện các loại rác thải 

Mô tả ngắn gọn: Đây là một ứng dụng nhận diện rác thải bằng YOLOv11, chạy trên giao diện web đơn giản – cho phép truy cập camera và nhận diện trực tiếp.

---

## 🚀 Tính năng chính

- Nhận diện rác qua webcam
- Sử dụng mô hình YOLOv11 tối ưu.
- Giao diện web đơn giản: bật/tắt nhận diện nhanh.
- Tùy biến nhãn tiếng Việt cho từng loại vật thể.
---
## 🏗️ Cấu trúc thư mục

```bash
yolo11-project/
├── backend/
│   ├── app.py          # Flask server
│   └── yolo11n.pt      # Trained YOLOv11 model
├── frontend/
│   ├── templates/
│   │   └── index.html
│   └── static/
│       └── css/
│           └── style.css
├── requirements.txt
  có thể tùy chỉnh css để phù hợp với giao diện web mong muốn 
