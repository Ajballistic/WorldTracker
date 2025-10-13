from flask import Flask, render_template
import json

app = Flask(__name__)

@app.route("/")
def index():
    with open('a6f2f5da-5773-4432-b7b4-8ec0b34a104a.json', 'r') as file:
        data = json.load(file)
    return render_template("index.html", stats = data["stats"])

if __name__ == "__main__":
    app.run()