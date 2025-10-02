from flask import Blueprint, jsonify
import requests

app = Blueprint('ssh', __name__)

@app.route('/ssh')

def ssh_check():
    try:
        r = requests.get('http://localhost:4040/api/tunnels', timeout=5)
        return jsonify(r.json())
    except requests.exceptions.RequestException as e:
        return f'<pre>Could not connect to ngrok API: {e}</pre>'
    except Exception as e:
        return f'<pre>Error: {e}</pre>'