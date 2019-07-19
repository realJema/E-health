from flask import Flask, render_template, request, session, url_for, redirect

app = Flask(__name__)
app.secret_key = 'whoknowsthissecretw'


# function for computation
def symptomes(feeling):
    feeling_data = {
                    'Dizzy':
                            [   ' Head ache',
                                ' Notious',
                                ' Feverish',
                                ' Inbalanced'],
                    'Ache':
                            [   ' Severe',
                                ' Mild',
                                ' Delocalised',
                                ' Average'],
                    'Tired':
                            [   ' Head ache',
                                ' Notious',
                                ' Feverish',
                                ' Inbalanced'],
                    'Anxious':
                            [   ' Severe',
                                ' Mild',
                                ' Delocalised',
                                ' Average']
                    }
    if feeling_data[feeling]:
        return feeling_data[feeling]
    else:
        return ['None Found']
def prescription(symptomes):
    ''' anaylse the symptomes of the user and determine the prescription to give him'''

    prescription_data = {
                        ' Head ache': 'Efferalgan',
                        ' Feverish' : 'Paracetamol',
                        ' Notious' : 'Paracetamol',
                        ' Inbalanced' : 'Paracetamol',
                        ' Severe' : 'Paracetamol',
                        ' Mild' : 'Paracetamol',
                        ' Delocalised' : 'Paracetamol',
                        ' Average' : 'Paracetamol'
                        }
    the_prescription = { }

    for symptome in symptomes:
        the_prescription[symptome] = prescription_data[symptome]

    print(the_prescription)

    return the_prescription
def infections(symptomes):
    ''' anaylse the symptomes of the user and determine the infections he has'''

    prescription_data = {
                        ' Head ache': 'Common Cold',
                        ' Feverish' : 'Common Cold',
                        ' Notious' : 'Parasite',
                        ' Inbalanced' : 'Virus',
                        ' Severe' : 'Virus',
                        ' Mild' : 'Virus',
                        ' Delocalised' : 'Virus',
                        ' Average' : 'Virus'
                        }
    the_Infections = { }

    for symptome in symptomes:
        the_Infections[symptome] = prescription_data[symptome]
    return the_Infections
# end of computation functions



# routing functions
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/terms')
def terms():
    return render_template('_02terms.html')

@app.route('/login')
def login():
    return render_template('_03login.html')

@app.route('/submission', methods=['GET', 'POST'])
def submission():

    session['login'] = True
    try:
        session['user'] = request.form['user']
        session['gender'] = request.form['gender']
        session['age'] = request.form['age']
    except:
        pass

    if request.method == 'POST':
        return render_template('_04qn1.html', user=session['user'])
    else:
        return redirect(url_for('index'))

@app.route('/qn1', methods=['GET', 'POST'])
def qn1():
    try:
        session['Weight'] = request.form['optionsWeight']
        session['Cigarettes'] = request.form['optionsCigarettes']
        session['Cholesterol'] = request.form['optionsCholesterol']
        session['Hypertension'] = request.form['optionsHypertension']
        session['Diabetes'] = request.form['optionsDiabetes']
    except:
        pass

    if request.method == 'POST':
        # the_symptomes = symptomes(session['feel'])
        return render_template('qn2.html')
    else:
        return redirect(url_for('welcome'))

@app.route('/qn2', methods=['GET', 'POST'])
def qn2():
    session['feel2'] = []

    # we will limit to 4 symptomes
    try:
        session['feel2'].append(request.form['optionsCheck0'])
    except:
        print('doesnt exist')
    try:
        session['feel2'].append(request.form['optionsCheck1'])
    except:
        print('doesnt exist')
    try:
        session['feel2'].append(request.form['optionsCheck2'])
    except:
        print('doesnt exist')
    try:
        session['feel2'].append(request.form['optionsCheck3'])
    except:
        print('doesnt exist')

    the_prescription = prescription(session['feel2'])
    the_Infections = infections(session['feel2'])
    return render_template('qn2.html', prescription=the_prescription, infections=the_Infections)

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