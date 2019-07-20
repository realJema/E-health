from flask import Flask, render_template, request, session, url_for, redirect

app = Flask(__name__)
app.secret_key = 'whoknowsthissecretw'

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
    return render_template('symptome2.html')

@app.route('/symptome3', methods=['GET', 'POST'])
def symptome3():
    return render_template('symptome3.html')

@app.route('/symptome4', methods=['GET', 'POST'])
def symptome4():
    return render_template('symptome4.html')

@app.route('/symptome5', methods=['GET', 'POST'])
def symptome5():
    return render_template('symptome5.html')

@app.route('/symptome6', methods=['GET', 'POST'])
def symptome6():
    return render_template('symptome6.html')

@app.route('/results', methods=['GET', 'POST'])
def results():
    return render_template('results.html')


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


if __name__ == '__main__':
    app.run(debug=True)