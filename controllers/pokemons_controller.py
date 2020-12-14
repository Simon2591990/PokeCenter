from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.pokemon import Pokemon
import repositories.pokemon_repository as pokemon_repository
import repositories.nurse_repository as nurse_repository
import repositories.trainer_repository as trainer_repository
import pdb

pokemon_blueprint = Blueprint("pokemon", __name__)

@pokemon_blueprint.route('/pokemon')
def pokemon():
    pokemons = pokemon_repository.select_all()
    return render_template('/pokemon/index.html', pokemons = pokemons)

@pokemon_blueprint.route('/pokemon/new')
def new_pokemon():
    trainers = trainer_repository.select_all()
    nurses = nurse_repository.select_all()
    return render_template('/pokemon/new.html', nurses = nurses, trainers = trainers)

@pokemon_blueprint.route('/pokemon', methods=['POST'])
def add_pokemon():
    nickname = request.form['nickname']
    species = request.form['species']
    type = request.form['type']
    dob = request.form['dob']
    trainer_id = request.form['trainer_id']
    status = request.form['status']
    nurse_id = request.form['nurse_id']

    trainer = trainer_repository.select(trainer_id)
    nurse = nurse_repository.select(nurse_id)
    pokemon = Pokemon(nickname, species, type, dob, trainer, status)
    pokemon.assign_nurse(nurse)
    
    pokemon_repository.save(pokemon)
    return redirect('/pokemon')

@pokemon_blueprint.route("/pokemon/<id>/delete", methods=['POST'])
def discharge_pokemon(id):
    pokemon_repository.delete(id)
    return redirect('/pokemon')

@pokemon_blueprint.route("/pokemon/<id>/edit")
def edit_pokemon_page(id):
    pokemon = pokemon_repository.select(id)
    nurses = nurse_repository.select_all()
    return render_template("/pokemon/edit.html", pokemon = pokemon, nurses = nurses)

@pokemon_blueprint.route("/pokemon/<id>/edit", methods=['POST'])
def edit_pokemon(id):
    nickname = request.form['nickname']
    species = request.form['species']
    type = request.form['type']
    dob = request.form['dob']
    trainer_name = request.form['trainer_name']
    trainer_number = request.form['trainer_number']
    status = request.form['status']
    nurse_id = request.form['nurse_id']

    nurse = nurse_repository.select(nurse_id)
    pokemon = Pokemon(nickname, species, type, dob, trainer_name, trainer_number, status, id)
    pokemon.assign_nurse(nurse)
    
    pokemon_repository.update(pokemon)
    return redirect('/pokemon')


