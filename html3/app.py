from flask import Flask, render_template, request, send_from_directory
import test
import sys,os.path
import subprocess
import wave

app = Flask(__name__)




# @app.route('/')
# def index():
# 	return render_template('index.html')

@app.route('/', methods = ["GET" , "POST"])
def index():
	if request.method == 'POST':
		print(a)
	return render_template('index.html') #6 GETの処理

@app.route('/rokuon', methods = ["GET" , "POST"])

def rokuon():
	if request.method == 'POST':
		if request.form.get('rokuon'):
			if request.form['rokuon'] == 'kaishi':
				print("Start recording...")
				cmd = "sox -t waveaudio -d audio\out.wav"
				global p
				p = subprocess.Popen(cmd.split())

				return render_template('rokuon.html', kaishi = "on")
			elif request.form['rokuon'] == 'teishi':
				p.terminate()
				try:
					p.wait(timeout=1)
				except subprocess.TimeoutExpired:
					p.kill()

				return render_template('rokuon.html', teishi = "off")
		elif request.form.get('data'):
			return render_template('rokuon.html', data = "読み込めました。")

	return render_template('rokuon.html')

@app.route('/fileread', methods = ["GET" , "POST"])
def fileread():
	if request.method == 'POST':
		file = request.files['music']
		fileName = file.filename
		return render_template('fileread.html', fileName = fileName)
	return render_template('fileread.html')

@app.route("/audio/<path:filename>")
def play(filename):
    return send_from_directory("audio", filename)


if __name__ == '__main__':
	app.run(host = '0.0.0.0', port = 8030, debug=True)


