from flask import Blueprint, request
from .discord import send_discord_message_trello
import os

trello_webhook = Blueprint("trello_webhook", __name__)

@trello_webhook.route("/webhook/trello/v1", methods=["HEAD", "GET", "POST"])
def handle_trello():
    if request.method in ["HEAD", "GET"]:
        return "Webhook verification", 200
    
    payload = request.json
    print("🧾 Webhook Trello gửi:", payload)

    try:
        action = payload.get("action", {})
        action_type = action.get("type", "")
        if action_type != "createCard":
            print("🔍 Bỏ qua action không phải createCard:", action_type)
            return "Ignored", 200

        data = action.get("data", {})
        card = data.get("card", {})

        task_name = card.get("name", "Không rõ")
        short_link = card.get("shortLink", "")
        url = f"https://trello.com/c/{short_link}" if short_link else "#"

        due_date = card.get("due", "Chưa có")  # chỉ có nếu đã set
        assignee = action.get("memberCreator", {}).get("fullName", "Không rõ")

        text = f"🆕 Task mới: **{task_name}**\n📅 Hạn: {due_date or 'Chưa có'}\n👤 Giao cho: {assignee}\n🔗 {url}"
        send_discord_message_trello(text)
        print("✅ Đã gửi thông báo đến Discord:", text)
    except Exception as e:
        print("❌ Lỗi xử lý webhook:", e)

    return "OK", 200
