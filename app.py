from flask import Flask

#(__name__) = "__main__" = executado de forma manual e nao importado d outro arquivo
app = Flask(__name__)

@app.route("/")
def helloworld():
    return "Hello World!"

@app.route("/about")
def about():
    return "Página sobre"

if __name__ == "__main__":
    app.run(debug=True)