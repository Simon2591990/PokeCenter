from flask import Flask, render_template, redirect, request
from flask import Blueprint
from models.trainer import Trainer
import repositories.trainer_repository as trainer_repository

trainers_blueprint = Blueprint("trainers", __name__)

@trainers_blueprint.route("/trainers")
def trainers():
    trainers = trainer_repository.select_all()
    return render_template("trainers/index.html", trainers = trainers)

@trainers_blueprint.route("/trainers/new")
def new_trainer():
    return render_template("/trainers/new.html")

@trainers_blueprint.route("/trainers", methods=['POST'])
def register_trainer():
    name = request.form['name']
    number = request.form['number']
    trainer = Trainer(name, number)
    trainer_repository.save(trainer)
    return redirect('/trainers')
