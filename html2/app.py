from flask import Flask, render_template, request

app = Flask(__name__)


# @app.route('/')
# def index():
# 	return render_template('index.html')

@app.route('/', methods = ["GET" , "POST"])
def index():
	if request.method == 'POST':
		name = request.form['name'] #4 formのname属性を取得
		return render_template('index.html', name=name) #5 screen_nameを代入
	return render_template('index.html') #6 GETの処理

if __name__ == '__main__':
	app.run(host = '0.0.0.0', port = 8050, debug=True)