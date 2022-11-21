from urllib.parse import urlparse

from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def hello_world():
    return f'<p>Hello from {urlparse(request.base_url).hostname}!</p>'

if __name__ == "__main__":
    app.run(debug=True)