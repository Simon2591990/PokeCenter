from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.pokemon import Pokemon
import repositories.pokemon_repository as pokemon_repository
import repositories.nurse_repository as nurse_repository
import pdb

pokemon_blueprint = Blueprint("pokemon", __name__)

@pokemon_blueprint.route('/pokemon')
def pokemon():
    pokemons = pokemon_repository.select_all()
    return render_template('/pokemon/index.html', pokemons = pokemons)

@pokemon_blueprint.route('/pokemon/new')
def new_pokemon():
    nurses = nurse_repository.select_all()
    return render_template('/pokemon/new.html', nurses = nurses)

@pokemon_blueprint.route('/pokemon', methods=['POST'])
def add_pokemon():
    nickname = request.form['nickname']
    species = request.form['species']
    type = request.form['type']
    dob = request.form['dob']
    trainer_name = request.form['trainer_name']
    trainer_number = request.form['trainer_number']
    status = request.form['status']
    nurse_id = request.form['nurse_id']

    nurse = nurse_repository.select(nurse_id)
    pokemon = Pokemon(nickname, species, type, dob, trainer_name, trainer_number, status)
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
    return render_template("/pokemon/<id>/edit.html", pokemon = pokemon)


