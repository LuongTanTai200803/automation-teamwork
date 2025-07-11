import re
from flask import Flask, json

from monolith_app import create_app
from monolith_app.github import github_webhook
from monolith_app.trello import trello_webhook
from monolith_app.cronjob import schedule_daily_report


app = create_app()
schedule_daily_report()


if __name__ == "__main__":
    app.run(port=5000, debug=True)
