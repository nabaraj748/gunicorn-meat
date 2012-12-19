from flask import Flask
from gunicorn_meat import Meat

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello Kenneth"

server = Meat(app,**{
    "workers" : 8
})

if __name__ == "__main__":
    server.run()
