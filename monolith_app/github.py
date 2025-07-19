from flask import Blueprint, request
from .discord import send_discord_message_github

github_webhook = Blueprint("github_webhook", __name__)

@github_webhook.route("/webhook/github/v1", methods=["POST"])
def handle_github():
    payload = request.json
    print(f"🧾 Webhook github gửi:{payload}" )

    # Kiểm tra đúng nhánh dev
    ref = payload.get("ref", "")

    # if ref != ["refs/heads/dev", "refs/heads/version_2", "refs/heads/version_1"]:
    #     return "Not dev branch", 200

    repo = payload.get("repository", {}).get("name", "unknown repo")
    pusher = payload.get("pusher", {}).get("name", "unknown user")
    commits = payload.get("commits", [])

    commit_messages = "\n".join(f"- {c['message']}" for c in commits) or "No commits"
    compare_url = payload.get("compare", "#")

    text = (
        f"🚀 **Push mới lên `{repo}` (nhánh dev)**\n"
        f"👤 Bởi: {pusher}\n"
        f"💬 Commit:\n{commit_messages}\n"
        f"🔗 {compare_url}"
    )

    send_discord_message_github(text)
    return "OK", 200
