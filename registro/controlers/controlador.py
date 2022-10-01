from registro import app
from flask import render_template, session, redirect, request


@app.route('/')
def contador():
    if "contador" not in session:
        session['contador'] = 0
    session['contador'] += 1
    return render_template('index.html', contador=session['contador'])


@app.route('/sumar1')
def sumar():
    return redirect('/')


@app.route('/reset')
def destruir():
    session.clear()
    return redirect('/')


@app.route('/sumar2')
def sumar2():
    session['contador'] += 1
    return redirect('/')


@app.route('/reinicio')
def reinicio():
    session['contador'] = 0
    return redirect('/')


@app.route('/sumarn', methods=['POST'])
def sumarn():
    session['contador'] += int(request.form['num'])-1
    return redirect('/')
