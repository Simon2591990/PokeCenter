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
def delete_pokemon(id):
    pokemon_repository.delete(id)
    return redirect('/pokemon')

@pokemon_blueprint.route("/pokemon/<id>/edit")
def edit_pokemon_page(id):
    pokemon = pokemon_repository.select(id)
    nurses = nurse_repository.select_all()
    trainers = trainer_repository.select_all()
    return render_template("/pokemon/edit.html", pokemon = pokemon, nurses = nurses, trainers = trainers)

@pokemon_blueprint.route("/pokemon/<id>/edit", methods=['POST'])
def edit_pokemon(id):
    nickname = request.form['nickname']
    species = request.form['species']
    type = request.form['type']
    dob = request.form['dob']
    trainer_id = request.form['trainer_id']
    status = request.form['status']
    nurse_id = request.form['nurse_id']

    trainer = trainer_repository.select(trainer_id)
    nurse = nurse_repository.select(nurse_id)
    pokemon = Pokemon(nickname, species, type, dob, trainer, status, id)
    pokemon.assign_nurse(nurse)
    
    pokemon_repository.update(pokemon)
    return redirect('/pokemon')

@pokemon_blueprint.route("/pokemon/<id>/discharge", methods=['POST'])
def discharge_pokemon(id):
    pokemon = pokemon_repository.select(id)
    pokemon.status = "Healthy"
    pokemon_repository.update(pokemon)
    return redirect("/pokemon/sick")

@pokemon_blueprint.route("/pokemon/sick")
def show_sick_pokemon():
    sick_pokemon = []
    pokemons = pokemon_repository.select_all()
    for pokemon in pokemons:
        if pokemon.status != "Healthy":
            sick_pokemon.append(pokemon)
    return render_template("pokemon/sick.html", pokemons = sick_pokemon)

@pokemon_blueprint.route("/pokemon/<id>/info")
def info(id):
    pokemons = []
    pokemons.append(pokemon_repository.select(id))
    return render_template("pokemon/info.html", pokemons = pokemons)

@pokemon_blueprint.route("/pokemon/info/", methods=['POST'])
def search():
    catagory = request.form['catagory']
    search = request.form['search']
    pokemons = pokemon_repository.search(catagory, search)
    return  render_template("pokemon/info.html", pokemons = pokemons)

@pokemon_blueprint.route("/pokemon/<species>/species")
def find_by_species(species):
    pokemons = pokemon_repository.search("species", species)
    return render_template("/pokemon/info.html", pokemons = pokemons)






