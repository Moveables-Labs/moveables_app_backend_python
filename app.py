from api import createApp
from utils.constants import Constants


app = createApp()


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"



#if __name__ == '__main__':
#    #app.run(debug=True,port=Constants.PORT)
