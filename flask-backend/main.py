import flask

app = flask.Flask("__main__")


@app.route('/')
def my_index():
    return flask.render_template("index.html", token="This is coming from a flask backend")


app.run(debug=True)
