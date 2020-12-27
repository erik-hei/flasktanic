from flask import Flask, render_template, request, jsonify, redirect
from data_science import make_model, test_model
import random

app=Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/results', methods=['POST'])
def results():
    global model
    global score

    (model, score) = make_model()
    score = round(score * 100, 1)

    name = request.form["Name"]
    title = request.form["Title"]
    if title.startswith("Mr"):
        title = title + "."

    Age = int(request.form["Age"])
    Is_female = int(request.form["Is_female"])
    Pclass = int(request.form["Pclass"])
    emb_C = int(request.form["Embarked"] == "C")
    emb_Q = int(request.form["Embarked"] == "Q")
    emb_S = int(request.form["Embarked"] == "S")
    Family_size = int(request.form["Family_size"])
    Mr = int(request.form["Title"] == "Mr")
    Mrs = int(request.form["Title"] == "Mrs")
    Master = int(request.form["Title"] == "Master")
    Miss = int(request.form["Title"] == "Miss")

    prob_survived = test_model(model, Age, Is_female, Pclass, emb_C, emb_Q, emb_S, 
                                Family_size, Mr, Mrs, Master, Miss)
    random_chance = random.random()
    survived = random_chance < prob_survived.item()
    prob_survived = round(prob_survived*100, 1)
    
    return render_template('results.html', score=score, name=name, title=title, 
                            prob_survived=prob_survived, survived=survived)
