import os
from apscheduler.schedulers.background import BackgroundScheduler
import requests
from .discord import send_discord_message_github, send_discord_message_trello
from datetime import datetime, timezone


# Tạm thời hardcode danh sách task
TASKS = [
    {"name": "Làm báo cáo tuần", "due": "2025-07-05"},
    {"name": "Fix bug giao diện", "due": "2025-07-09"},
    {"name": "Tạo video demo", "due": "2025-07-12"}
]

TRELLO_KEY = os.getenv("TRELLO_API_KEY")
TRELLO_TOKEN = os.getenv("TRELLO_TOKEN")
TRELLO_BOARD_ID = os.getenv("TRELLO_BOARD_ID")

def get_cards_from_trello():
    url = f"https://api.trello.com/1/boards/{TRELLO_BOARD_ID}/cards"
    params = {"key": TRELLO_KEY, "token": TRELLO_TOKEN}
    response = requests.get(url, params=params)

    if response.status_code == 200:
        return response.json()
    else:
        print(" Không thể lấy danh sách card từ Trello:", response.text)
        return []
    
def daily_summary():
    cards = get_cards_from_trello()
    now = datetime.now(timezone.utc)

    overdue_tasks = []
    for card in cards:
        if card.get("due") and not card.get("closed"):
            try:
                due_date = datetime.fromisoformat(card["due"].replace("Z", "+00:00"))
                if due_date < now:
                    overdue_tasks.append(f"- {card['name']} (Hạn: {due_date.date()})")
            except Exception as e:
                print(" Lỗi xử lý ngày:", e)

    if overdue_tasks:
        text = "❗ Task quá hạn:\n" + "\n".join(overdue_tasks)
        send_discord_message_trello(text)
    else:
        print("✅ Không có task nào quá hạn.")

def schedule_daily_report():
    scheduler = BackgroundScheduler()
    # Test 'interval', seconds=30  / 'cron', hour=8
    scheduler.add_job(daily_summary, 'cron', hour=8)
    scheduler.start()
    print("✅ Đã lên lịch báo cáo hàng ngày.")

