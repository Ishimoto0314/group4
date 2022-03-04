from flask import Flask, render_template, request, send_from_directory
import test
import sys,os.path
import subprocess
import wave
import numpy as np
import libProcess
import librosa
import pandas as pd


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
				cmd = "sox -t waveaudio -d -r 44100 audio\1.wav"
				global p
				p = subprocess.Popen(cmd.split(), shell=True)

				return render_template('rokuon.html', kaishi = "on")
			elif request.form['rokuon'] == 'teishi':
				p.terminate()
				try:
					p.wait(timeout=1)
				except subprocess.TimeoutExpired:
					p.kill()

				return render_template('rokuon.html', teishi = "off")
		elif request.form.get('start'):
			array = libProcess.process() #解析の実行
			return render_template('down.html', array = array)

	return render_template('rokuon.html')

@app.route('/fileread', methods = ["GET" , "POST"])
def fileread():
	if request.method == 'POST':
		file = request.files['music'] #音楽データの受け取り
		fileext = os.path.splitext(file.filename)[1]
		print(fileext)
		if fileext == (".webm"):
			deletefile = 'audio/1.wav'
			os.remove(deletefile)
			file.save("audio/2.webm")
			targetfile = 'audio/2.webm'
			cmd = 'ffmpeg -i {} -vn audio/1.wav'.format(targetfile)
			subprocess.run(cmd, shell=True)

		else:
			file.save("audio/1.wav")
		array = libProcess.process() #解析の実行
		return render_template('down.html', array = array)
	return render_template('fileread.html')

@app.route("/audio/<path:filename>")
def play(filename):
    return send_from_directory("audio", filename)


@app.route('/down', methods = ["GET" , "POST"]) #pdfをダウンロードするページ
def down():
	if request.method == 'POST':
		
		return render_template('down.html')
	return render_template('down.html')

@app.route("/pdf/<path:filename>")
def pdf(filename):
    return send_from_directory("pdf", filename)


if __name__ == '__main__':
	app.run(host = '0.0.0.0', port = 8030, debug=True)


