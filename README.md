# YOLO11 để nhận diện các loại rác thải 

Mô tả ngắn gọn: Đây là một ứng dụng nhận diện rác thải bằng YOLOv11, chạy trên giao diện web đơn giản – cho phép truy cập camera và nhận diện trực tiếp.

---

## Tính năng chính

- Nhận diện rác qua webcam
- Sử dụng mô hình YOLOv11 tối ưu.
- Giao diện web đơn giản: bật/tắt nhận diện nhanh.
---
## Cấu trúc thư mục

```bash
yolo11-project/
├── backend/
│   ├── webnhandien.py          # Flask server
│   └── yolo11n.pt      # mô hình đã train có thể thay bằng mô hình train khác
├── frontend/
│   ├── templates/
│   │   └── index.html
│   └── static/   # có thể thêm để web thêm phong cách
│       └── css/
│           └── style.css
├── requirements.txt
