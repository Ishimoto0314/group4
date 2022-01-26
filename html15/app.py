from flask import Flask, jsonify, request, render_template
from datetime import datetime
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html") # templatesフォルダ内のindex.htmlを表示する

@app.route('/wav', methods=['POST'])
def wav():
    fname = "sounds/" + datetime.now().strftime('%m%d%H%M%S') + ".wav"
    with open(f"{fname}", "wb") as f:
        f.write(request.files['audio_data'].read())
    print(f"posted sound file: {fname}")
    return jsonify({"audio_data": fname})


if __name__ == "__main__":
    app.run()