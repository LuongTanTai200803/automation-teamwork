from flask import Flask
from monolith_app.trello import trello_webhook  
from monolith_app.github import github_webhook

def create_app():
    app = Flask(__name__)

    app.register_blueprint(github_webhook)
    app.register_blueprint(trello_webhook)

    # print("📌 Các route đang hoạt động:")
    # for rule in app.url_map.iter_rules():
    #     print(rule)
    
    return app
