from flask import Flask, render_template, request, session, redirect, url_for
import re

app = Flask(__name__)
app.secret_key = 'any random string'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    text = request.form['text']
    num_words = len(text.split())
    num_chars = len(text)
    num_nums = len(re.findall(r'\d+', text))
    special_chars = len(re.findall('[^a-zA-Z0-9\s]',text))
    session['num_words'] = num_words
    session['num_chars'] = num_chars
    session['num_nums'] = num_nums
    session['special_chars'] = special_chars
    return render_template('analyze.html')

@app.route('/words', methods = ['POST','GET'])
def words():
    return render_template('words.html', count=session.get('num_words'),backurl=url_for("index"))

@app.route('/chars', methods = ['POST','GET'])
def chars():
    return render_template('chars.html', count=session.get('num_chars'),backurl=url_for("index"))

@app.route('/nums', methods = ['POST','GET'])
def nums():
    return render_template('nums.html', count=session.get('num_nums'),backurl=url_for("index"))

@app.route("/special_chars", methods = ['POST','GET'])
def special_chars():
    return render_template("special_chars.html", count=session.get('special_chars'),backurl=url_for("index"))


if __name__ == '__main__':
    app.run(debug=True)
