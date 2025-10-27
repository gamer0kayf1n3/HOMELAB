from webserver import create_app
import os

if os.path.exists("DEBUG"):
    debug = True
    port = 81
else:
    debug = False
    port = 80

app = create_app()

if __name__ == "__main__":
    app.run(port=port, host='0.0.0.0', debug=debug)