from gunicorn_meat import Meat

server = Meat('test_gunicorn_meat:app',**{
    "workers" : 8
})

if __name__ == "__main__":
    server.run()