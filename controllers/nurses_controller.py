from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.nurse import Nurse
import repositories.nurse_repository as nurse_repository

nurses_blueprint = Blueprint("nurses", __name__)

@nurses_blueprint.route("/staff")
def staff():
    nurses = nurse_repository.select_all()
    return render_template("staff/index.html", nurses = nurses)