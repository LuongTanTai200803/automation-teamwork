## 1. GitHub Push → Discord

**Trigger**: Khi có push mới lên nhánh `dev` trong GitHub  
**Flow:**
- GitHub gửi webhook đến `/webhook/github`
- Flask nhận JSON và trích xuất:
  - Người push
  - Tin nhắn commit
  - URL commit
- Gửi message lên Discord qua Webhook

**Kênh gửi**: `#dev-updates`

---

## 2. Trello Task mới → Discord

**Trigger**: Khi có task mới tạo trên Trello  
**Flow:**
- Trello gửi webhook đến `/webhook/trello`
- Flask trích xuất:
  - Tên task
  - Người được giao
  - Deadline
  - URL Trello
- Gửi message ping người nhận

**Kênh gửi**: `#task-tracker`

---

## 3. Cron Task – Gửi báo cáo hàng ngày

**Trigger**: Hàng ngày lúc 08:00  
**Flow:**
- APScheduler chạy `daily_summary()`
- Lọc các task quá hạn từ danh sách
- Gửi báo cáo liệt kê các task quá hạn

**Kênh gửi**: `#daily-report`

---

## 4. Sơ đồ luồng (vẽ bằng draw.io hoặc diagrams.net)
[GitHub Push] -->> [Flask webhook/github] -->> [Discord Message]
^
|
[Trello Task Created] -->> [Flask webhook/trello] -->> [Discord Message]
^
|
[Scheduler 08:00] -->> [Check overdue] -->> [Discord báo cáo task quá hạn]

## 5. Lưu ý kỹ thuật

- Các webhook là POST JSON, header: `Content-Type: application/json`
- Để test webhook: dùng Postman hoặc curl
- Webhook Discord chỉ gửi được vào kênh đã cấu hình
- Task cron có thể test bằng `interval` trước khi dùng `cron`

---