##  Tính năng đề xuất:

- [ ] Chuyển từ Discord Webhook sang Bot thật (gửi tin nhắn nâng cao, ping user, gửi file)
- [ ] Tích hợp trực tiếp API Trello để đọc danh sách task động thay vì hardcode
- [ ] Thêm hệ thống gán nhãn ưu tiên (High / Medium / Low) cho task
- [ ] Tách các webhook (GitHub, Trello, Cron) thành từng service nhỏ (microservices)
- [ ] Viết unit test cho endpoint và Discord push
- [ ] Dùng Redis hoặc SQLite để lưu trạng thái task

##  Ghi chú nhanh:
- Khi làm microservice → có thể dùng Flask + Docker riêng từng phần
- Nếu dùng bot thật → phải tạo bot Discord và lấy token