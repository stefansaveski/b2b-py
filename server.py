from flask import Flask, render_template, request, session, redirect, url_for
from moduleFunc import save_submission_to_json
from MAINscript import start
from datetime import datetime

app = Flask(__name__, template_folder='templates')
app.secret_key = "B2BWEB"

@app.route('/')
def index():
    if "index_redirected" in session:
        return render_template('zadaca1.html')
    elif "index" in session:
        session["index_redirected"] = True
        return redirect(url_for('zadaca1'))
    else:
        return render_template('index.html')

@app.route('/zadaca1/')
def zadaca1():
    if request.method == 'POST':
        flash('Action successful', 'success')
        return redirect(url_for('zadaca1'))
    return render_template('zadaca1.html')

@app.route('/zadaca2/')
def zadaca2():
    return render_template('zadaca2.html')

@app.route('/zadaca3/')
def zadaca3():
    return render_template('zadaca3.html')

@app.route('/quizend/')
def quizend():
    return render_template('quizend.html')

@app.route('/process_code', methods=['POST'])
def process_code():
    data = request.get_json()
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    return start(data, session["index"], session["name"], session['start_time'], current_time)

@app.route('/login', methods=['POST'])
def login():
    if "index" in session:
        return redirect(url_for('zadaca1'))
    data = request.get_json()
    print(data)
    session["index"] = data.get("jsonData", {}).get("index", '')
    session["name"] = str(data.get("jsonData", {}).get("name", '')) + " " + str(data.get("surname", ''))
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    session['start_time'] = current_time
    return "true"

if __name__ == '__main__':
    app.run(port=8000, debug=True)