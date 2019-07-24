from flask import Flask, render_template, request, session, url_for, redirect
from flask_socketio import SocketIO

app = Flask(__name__)
app.secret_key = 'whoknowsthissecretw'
socketio = SocketIO(app)

''' This is a list of all variables
    session['login'] = True
    session['user'] = request.form['user']
    session['gender'] = request.form['gender']
    session['age'] = request.form['age']
    session['obesity'] = request.form['optionsWeight']
    session['cigar'] = request.form['optionsCigarettes']
    session['chol'] = request.form['optionsCholesterol']
    session['hypert'] = request.form['optionsHypertension']
    session['diabetes'] = request.form['optionsDiabetes']
    session['illRange'] = request.form['optionsRange']
    session['duration']  = request.form['optionsDuration']
    session['trauma']  = request.form['optionsTrauma']
    session['fever']  = request.form['optionsFever']

'''

# routing functions
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/terms')
def terms():
    return render_template('terms.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/symptome1', methods=['GET', 'POST'])
def symptome1():

    session['login'] = True
    try:
        session['user'] = request.form['user']
        session['gender'] = request.form['gender']
        session['age'] = request.form['age']
    except:
        pass

    return render_template('symptome1.html', user=session['user'])

@app.route('/symptome2', methods=['GET', 'POST'])
def symptome2():
    try:
        session['obesity'] = request.form['optionsWeight']
        session['cigar'] = request.form['optionsCigarettes']
        session['chol'] = request.form['optionsCholesterol']
        session['hypert'] = request.form['optionsHypertension']
        session['diabetes'] = request.form['optionsDiabetes']
    except:
        pass

    return render_template('symptome2.html')

@app.route('/symptome3', methods=['GET', 'POST'])
def symptome3():
    return render_template('symptome3.html')

@app.route('/symptome4', methods=['GET', 'POST'])
def symptome4():
    try:
        session['illRange'] = request.form['optionsRange']
    except:
        pass

    print(session['illRange'])
    return render_template('symptome4.html')

@app.route('/symptome5', methods=['GET', 'POST'])
def symptome5():
    try:
        session['duration']  = request.form['optionsDuration']
    except:
        pass

    return render_template('symptome5.html')

@app.route('/symptome6', methods=['GET', 'POST'])
def symptome6():
    try:
        session['trauma']  = request.form['optionsTrauma']
    except:
        pass

    return render_template('symptome6.html')

@app.route('/results', methods=['GET', 'POST'])
def results():
    try:
        session['fever']  = request.form['optionsFever']
    except:
        pass


    return render_template('results.html', user = session['user'], gender = session['gender'], age = session['age'], obesity = session['obesity'], cigar = session['cigar'], chol = session['chol'], hypert = session['hypert'], diabetes = session['diabetes'], illRange = session['illRange'], duration = session['duration'],  trauma = session['trauma'],  fever = session['fever'] )


# Routes for first aid pages
@app.route('/firstAid')
def firstAid():
    return render_template('first-aid.html')

# bleeding pages
@app.route('/bleeding_1')
def bleeding_1():
    return render_template('bleeding/bleeding_1.html')
@app.route('/bleeding_2')
def bleeding_2():
    return render_template('bleeding/bleeding_2.html')
@app.route('/bleeding_3')
def bleeding_3():
    return render_template('bleeding/bleeding_3.html')
@app.route('/bleeding_4')
def bleeding_4():
    return render_template('bleeding/bleeding_4.html')
@app.route('/bleeding_5')
def bleeding_5():
    return render_template('bleeding/bleeding_5.html')
@app.route('/bleeding_6')
def bleeding_6():
    return render_template('bleeding/bleeding_6.html')

# cpr pages
@app.route('/cpr_1')
def cpr_1():
    return render_template('cpr/cpr_1.html')
@app.route('/cpr_2')
def cpr_2():
    return render_template('cpr/cpr_2.html')
@app.route('/cpr_3')
def cpr_3():
    return render_template('cpr/cpr_3.html')
@app.route('/cpr_4')
def cpr_4():
    return render_template('cpr/cpr_4.html')
@app.route('/cpr_5')
def cpr_5():
    return render_template('cpr/cpr_5.html')
@app.route('/cpr_6')
def cpr_6():
    return render_template('cpr/cpr_6.html')

@app.route('/doctor')
def doctor():
    return render_template('doctor.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/logout')
def logout():
    del session['user']
    session['login'] = False
    return redirect(url_for('index'))

@app.route('/ajaxcall', methods=['GET', 'POST'])
def ajaxcall():
    student_id = request.args.get("student_id")
    return "Helloworld"

@app.errorhandler(404)
def page_not_found(error):
    return render_template('error.html'), 404

def messageReceived(methods=['GET', 'POST']):
    print('message was received!!!')


@socketio.on('my event')
def handle_my_custom_event(json, methods=['GET', 'POST']):
    # print('received my event: ' + str(json))
    socketio.emit('my response', json, callback=messageReceived)


if __name__ == '__main__':
    socketio.run(app, debug=True)
