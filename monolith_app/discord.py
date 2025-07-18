import os
import requests
from dotenv import load_dotenv

load_dotenv()
DISCORD_URL_TRELLO = os.getenv("DISCORD_URL_TRELLO")
DISCORD_URL_GITHUB = os.getenv("DISCORD_URL_GITHUB")
print("DISCORD_URL_TRELLO:", DISCORD_URL_TRELLO)
print("DISCORD_URL_GITHUB:", DISCORD_URL_GITHUB)
def send_discord_message_trello(content: str):
    if not DISCORD_URL_TRELLO:
        print(" DISCORD_URL_TRELLO chưa được cấu hình.")
        return
    requests.post(DISCORD_URL_TRELLO, json={"content": content})
    print("Đã gửi tin nhắn đến Discord:", content)

def send_discord_message_github(content: str):
    if not DISCORD_URL_GITHUB:
        print(" DISCORD_URL_GITHUB chưa được cấu hình.")
        return
    requests.post(DISCORD_URL_GITHUB, json={"content": content})