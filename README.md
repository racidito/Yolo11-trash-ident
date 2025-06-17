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
```
## Hương dẫn dùng
- cài đặt các thư viện trong requirements.txt
- đảm bảo chạy file ở đúng thư mục và cấu trúc trên
- chạy webnhandien.py và truy cập http://localhost:1503/ để truy cập web
- bấm "Bật nhận diện" rồi đợi một lúc để mô hình loading
- dùng thử chai nhựa để trước webcam để kiểm tra khả năng nhận diện
