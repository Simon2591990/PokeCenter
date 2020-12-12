from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.pokemon import Pokemon
import repositories.pokemon_repository as pokemon_repository

pokemon_blueprint = Blueprint("pokemon", __name__)

@pokemon_blueprint.route('/pokemon')
def pokemon():
    pokemons = pokemon_repository.select_all()
    return render_template('/pokemon/index.html', pokemons = pokemons)

