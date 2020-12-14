from db.run_sql import run_sql
import pdb

from models.pokemon import Pokemon
from models.nurse import Nurse
import repositories.nurse_repository as nurse_repository

def save(pokemon):
    sql = "INSERT INTO pokemons (nickname, species, type, dob, trainer_id, status, nurse_id) VALUES (%s, %s, %s, %s, %s, %s, %s) RETURNING *"
    values = [pokemon.nickname, pokemon.species, pokemon.type, pokemon.dob, pokemon.trainer.id, pokemon.status, pokemon.nurse.id]
    results = run_sql(sql, values)
    id = results[0]['id']
    pokemon.id = id
    return pokemon


def delete_all():
    sql = "DELETE FROM pokemons"
    run_sql(sql)


def delete(id):
    sql = "DELETE FROM pokemons WHERE id = %s"
    values = [id]
    run_sql(sql, values)


def select_all():
    pokemons = []
    sql = "SELECT * FROM pokemons"
    results = run_sql(sql)
    for row in results:
        nurse = nurse_repository.select(row['nurse_id'])
        pokemon = Pokemon(row['nickname'], row['species'], row['type'], row['dob'], row['trainer_id'], row['status'], row['id'])
        pokemon.assign_nurse(nurse)
        pokemons.append(pokemon)
    return(pokemons)


def select(id):
    pokemon = None
    sql = "SELECT * FROM pokemons WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        # pdb.set_trace()
        nurse = nurse_repository.select(result['nurse_id'])
        pokemon = Pokemon(result['nickname'], result['species'], result['type'], result['dob'], result['trainer_name'], result['trainer_number'], result['status'], result['id'])
        pokemon.assign_nurse(nurse)
    return pokemon


def update(pokemon):
    sql = "UPDATE pokemons SET (nickname, species, type, dob, trainer_id, status, nurse_id) = (%s, %s, %s, %s, %s, %s, %s, %s) WHERE id = %s RETURNING *"
    values = [pokemon.nickname, pokemon.species, pokemon.type, pokemon.dob, pokemon.trainer.id, pokemon.status, pokemon.nurse.id, pokemon.id]
    run_sql(sql, values)