from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.nurse import Nurse
import repositories.nurse_repository as nurse_repository

nurses_blueprint = Blueprint("nurses", __name__)

@nurses_blueprint.route("/staff")
def staff():
    nurses = nurse_repository.select_all()
    return render_template("staff/index.html", nurses = nurses)

@nurses_blueprint.route("/staff/new")
def new_nurse():
    return render_template("/staff/new.html")

@nurses_blueprint.route("/staff", methods=['POST'])
def add_nurse():
    name = request.form['name']
    nurse = Nurse(name)
    nurse_repository.save(nurse)
    return redirect('/staff')

@nurses_blueprint.route("/staff/<id>/delete", methods=['POST'])
def remove_nurse(id):
    nurse_repository.delete(id)
    return redirect('/staff')

@nurses_blueprint.route("/staff/<id>/edit")
def edit_nurse_form(id):
    nurse = nurse_repository.select(id)
    return render_template("/staff/edit.html", nurse = nurse)

@nurses_blueprint.route("/staff/<id>/edit", methods=['POST'])
def edit_nurse(id):
    name = request.form['name']
    nurse = Nurse(name, id)
    nurse_repository.update(nurse)
    return redirect('/staff')
    