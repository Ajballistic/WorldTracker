from flask import Flask, render_template
import json
import copy

app = Flask(__name__)

@app.route("/")
def index():
    with open('a6f2f5da-5773-4432-b7b4-8ec0b34a104a.json', 'r') as file:
        data = json.load(file)
        new_data = copy.deepcopy(data)
        for stat_type in data["stats"]:
            new_data["stats"][stat_type.replace("minecraft:","")] = new_data["stats"].pop(stat_type)
    return render_template("index.html", stats = new_data["stats"])

if __name__ == "__main__":
    app.run()