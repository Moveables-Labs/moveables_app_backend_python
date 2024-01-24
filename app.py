from api.extensions import createApp

app = createApp()


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


if __name__ == '__main__':
    # app.run(debug=True, port=Constants.PORT)
    # app.run(debug=False, host='0.0.0.0')
    from waitress import serve
    serve(app, host="0.0.0.0", port=8080)
