from flask import Flask, render_template, request, jsonify, redirect
from data_science import make_model, model_score, test_model
import random

app=Flask(__name__)

model = make_model()
score = model_score(model)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/results', methods=['POST'])
def results():
    model = make_model()
    score = model_score(model)
    score = round(score * 10, 1)

    name = request.form["Name"]
    title = request.form["Title"]
    if title.startswith("Mr"):
        title = title + "."

    Age = int(request.form["Age"])
    Is_female = int(request.form["Is_female"])
    Pclass = int(request.form["Pclass"])
    emb_C = int(request.form["embarked"] == "C")
    emb_Q = int(request.form["embarked"] == "Q")
    emb_S = int(request.form["embarked"] == "S")
    Family_size = int(request.form["Family_size"])
    Mr = int(request.form["Title"] == "Mr")
    Mrs = int(request.form["Title"] == "Mrs")
    Master = int(request.form["Title"] == "Master")
    Miss = int(request.form["Title"] == "Miss")

    prob_survived = test_model(model, Age, Is_female, Pclass, emb_C, emb_Q, emb_S, 
                                Family_size, Mr, Mrs, Master, Miss)
    random_chance = random.random()
    survived = random < prob_survived
    
    return render_template('results.html', score=score, name=name, title=title, 
                            prob_survived=prob_survived, survived=survived)
