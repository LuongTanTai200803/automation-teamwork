from unittest.mock import patch

from monolith_app import create_app

from task_helper import filter_overdue_tasks
from datetime import datetime, timedelta, timezone

def test_filter_overdue_tasks():
    now = datetime(2025, 7, 9, 8, 0, 0 ,tzinfo=timezone.utc)  # cố định thời điểm hiện tại

    mock_cards = [
        {"name": "Task 1", "due": "2025-07-08T09:00:00Z"},  # Quá hạn
        {"name": "Task 2", "due": "2025-07-09T10:00:00Z"},  # Chưa quá hạn
        {"name": "Task 3", "due": None},                    # Không có hạn
        {"name": "Task 4", "due": "2025-07-07T12:00:00Z"}   # Quá hạn
    ]

    result = filter_overdue_tasks(mock_cards, now)
    assert result == ["Task 1", "Task 4"]

@patch("monolith_app.github.send_discord_message_github")
def test_github_webhook(mock_send):
    app = create_app()
    client = app.test_client()

    payload = {
        "ref": "refs/heads/dev",
        "commits": [
            {"message": "Update README", "url": "https://github.com/..."}
        ],
        "repository": {"full_name": "username/repo"}
    }

    response = client.post("/webhook/github/v1", json=payload)
    assert response.status_code == 200


@patch("monolith_app.trello.send_discord_message_trello")
def test_trello_webhook(mock_send):
    app = create_app()
    client = app.test_client()

    payload = {
            "action": {
                "type": "createCard",
                "data": {
                    "card": {
                        "name": "Task Test",
                        "shortLink": "abc123",
                        "due": "2025-07-12"
                    }
                },
                "memberCreator": {
                    "fullName": "Tài"
                }
            }
        }

    response = client.post("/webhook/trello/v1", json=payload)
    assert response.status_code == 200