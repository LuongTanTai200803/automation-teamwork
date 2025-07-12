
from monolith_app import create_app
from monolith_app.cronjob import schedule_daily_report

app = create_app()
schedule_daily_report()

@app.route('/')
def home():
    return "Hello, Flask with Docker!"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000)