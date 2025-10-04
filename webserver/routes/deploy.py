from flask import Blueprint, request, jsonify
import os
from pprint import pprint
import psutil

from dotenv import load_dotenv, find_dotenv
load_dotenv(".env")
DEPLOY_SECRET = os.getenv("DEPLOY_SECRET")

from subprocess import Popen

app = Blueprint('deploy', __name__)

@app.route('/deploy', methods=['GET', 'POST'])
def stats():
    # detect if get or post
    if request.method != "POST":
        return "Why are you here?"
    print(request.headers.get("X-Github-Encoded-Secret"))
    print(DEPLOY_SECRET)
    if request.headers.get('X-Github-Encoded-Secret') != DEPLOY_SECRET:
        print("It's not GitHub")
        return "Deploy failed!", 401
    print("It's GitHub!")
    Popen([r"C:\Users\rfont\HOMELAB\deploy.bat"])
    return "Deploy sequence initiated."

