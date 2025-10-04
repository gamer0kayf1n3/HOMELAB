from flask import Blueprint, request, jsonify
import os
from pprint import pprint
import psutil

from dotenv import load_dotenv, find_dotenv
load_dotenv(".env")
DEPLOY_SECRET = os.getenv("DEPLOY_SECRET")

import subprocess

app = Blueprint('deploy', __name__)

import hashlib
import hmac
def verify_signature(payload_body, secret_token, signature_header):
    """Verify that the payload was sent from GitHub by validating SHA256.

    Raise and return 403 if not authorized.

    Args:
        payload_body: original request body to verify (request.body())
        secret_token: GitHub app webhook token (WEBHOOK_SECRET)
        signature_header: header received from GitHub (x-hub-signature-256)
    """
    if not signature_header:
        return "header was missing",403
    hash_object = hmac.new(secret_token.encode('utf-8'), msg=payload_body, digestmod=hashlib.sha256)
    expected_signature = "sha256=" + hash_object.hexdigest()
    print(f"{expected_signature=}")
    if not hmac.compare_digest(expected_signature, signature_header):
        return "mismatch in hash",403
    return True

@app.route('/deploy', methods=['GET', 'POST'])
def stats():
    # detect if get or post
    if request.method != "POST":
        return "Why are you here?"
    print( request.headers.get("X-Hub-Signature-256"))
    print(request.headers)
    signature = verify_signature(request.data, DEPLOY_SECRET, request.headers.get("X-Hub-Signature-256"))
    if signature != True: return signature
    print("It's GitHub!")
    subprocess.Popen(["cmd.exe", "/c", "start", "", r"C:\Users\rfont\HOMELAB\deploy.bat"],
    creationflags=subprocess.DETACHED_PROCESS | subprocess.CREATE_NEW_PROCESS_GROUP)
    return "Deploy sequence initiated."

