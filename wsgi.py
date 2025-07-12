
from monolith_app import create_app
from monolith_app.cronjob import schedule_daily_report

app = create_app()
schedule_daily_report()