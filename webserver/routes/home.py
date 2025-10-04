from flask import Blueprint

app = Blueprint('home', __name__)

@app.route('/')
def home():
    return '''
    You are now at 0kayf1n3's page. Say hi at <a href="https://twitter.com/@0kayf1n3">Twitter</a>. 
    Convenience pages: <a href="/stats">stats</a>
    <br>
    This server is running v1.0.0.
    '''