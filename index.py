from flask import Flask, render_template, request
import pyfiglet


app = Flask(__name__)

@app.route("/")
def home():
    text = request.args.get("text")
    result = ""
    if not text:
        text = ""
    else:
        result = pyfiglet.figlet_format(text)
    return render_template("index.html", text=text, result=result)