from flask import Flask

app = Flask(__name__)
@app.route("/data")
def members():
    return "hello"

if __name__=="__main__":
    app.run(debug=True)
