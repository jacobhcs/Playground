from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
  return render_template('index.html', phrase="Hello", times=5)

@app.route('/play')
def play():
  return render_template('play.html', phrase='Hello', times=3)

@app.route('/play/<int:num>')
def multiply(num):
  return render_template('multiply.html', num=num)

@app.route('/play/<int:num>/<string:color>')
def pickcolor(num,color):
  return render_template('color.html', num=num, color=color)

if __name__=="__main__":
  app.run(debug=True)