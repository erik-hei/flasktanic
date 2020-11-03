from flask import Flask, render_template, request, jsonify, redirect

app=Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/results', methods=['GET', 'POST'])
def results():
    if request.method == 'POST':
        user_data = request.form
        # run some data sciency stuf here
        return redirect('/results')
    else:
        return render_template('results.html')