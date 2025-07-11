import os
import requests
from dotenv import load_dotenv

load_dotenv()
DISCORD_URL = os.getenv("DISCORD_WEBHOOK_URL")
DISCORD_URL_1 = os.getenv("DISCORD_WEBHOOK_URL_1")

def send_discord_message_trello(content: str):
    if not DISCORD_URL:
        print(" DISCORD_WEBHOOK_URL chưa được cấu hình.")
        return
    requests.post(DISCORD_URL, json={"content": content})


def send_discord_message_github(content: str):
    if not DISCORD_URL:
        print(" DISCORD_WEBHOOK_URL_1 chưa được cấu hình.")
        return
    requests.post(DISCORD_URL_1, json={"content": content})