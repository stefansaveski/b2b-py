from flask import Flask, render_template, request, session, redirect, url_for
from moduleFunc import save_submission_to_json
from MAINscript import start
from datetime import datetime

app = Flask(__name__, template_folder='templates')
app.secret_key = "B2BWEB"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/zadaca1/')
def zadaca1():
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
    try:
        return start(data, session["index"], session["name"], session['start_time'], current_time)
    except:
        return {"input": ' ', "expected": ' ',"got": ' ', "is_same": ' ', "correct": ' ', "CompilationError": 'Server error try again'}

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    print(data)
    session["index"] = data.get("jsonData", {}).get("index", '')
    session["name"] = str(data.get("jsonData", {}).get("name", '')) + " " + str(data.get("jsonData", {}).get("surname", ''))
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    session['start_time'] = current_time
    return "true"

@app.route('/get_page', methods=['POST'])
def get_page():
    data =  request.get_json()
    code = "code" + str(data.get("jsonData", {}).get("zadaca", ''))
    table = "table" + str(data.get("jsonData", {}).get("zadaca", ''))
    if code in session and table in session:
        return {"code":session[code], "table":session[table], "get":" "}
    else:
        return {"code":" ", "table":" ", "get":"empty"}
 
@app.route('/save_page', methods=['POST'])
def save_page():
    data = request.get_json()
    zadaca = data.get("jsonData", {}).get("zadaca", '')
    session["code"+str(zadaca)] = data.get("jsonData", {}).get("cpp_code", '')
    session["table" + str(zadaca)] = data.get("jsonData", {}).get("table", '')
    return "true"


if __name__ == '__main__':
    app.run(port=8000, debug=True)