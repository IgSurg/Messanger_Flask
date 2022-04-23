from flask import Flask

app = Flask(__name__)


#config = {
#        "port": os.environ.get('PORT', 8080),
#        "debug": os.environ.get('DEBUG', False)
#}

# if set to true will return only a "Hello World" string.
Debug = True

# start a route to the index part of the app in flask.
@app.route('/')
def index():
    if (Debug == True):
        return 'Hello World!'
    else:
        pass


if __name__ == "__main__":
    app.run(host='0.0.0.0', port =5000)

#    app.run(host="0.0.0.0", port=config["port"], debug=config["debug"])