##  Mục tiêu dự án

Giải quyết vấn đề chậm trễ giao tiếp trong các nhóm dev nhỏ khi:
- Có người push code mà không báo
- Task Trello không ai để ý
- Task trễ hạn không ai theo dõi

### Giải pháp

- Dùng webhook GitHub → Discord
- Dùng webhook Trello → Discord
- Cron job hàng ngày → Discord
- Tất cả dùng Flask + APScheduler + Webhook Discord

# Discord Notification Automation

Tự động thông báo ở Server Discord khi có:
- Push mới lên GitHub (nhánh `dev`)
- Task mới trên Trello
- Task trễ hạn mỗi ngày lúc 8h sáng

##  Công nghệ:
- Python + Flask
- APScheduler
- Discord Webhook
- .env cấu hình

##  Cài đặt (Local)

# 1. Clone project
git clone https://github.com/LuongTanTai200803/automation-teamwork.git
cd monolith_app/

# 2. Tạo môi trường ảo & cài package
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# 3. Tạo file .env từ mẫu
cp .env.example .env

# 4. Chạy local
python3 main.py