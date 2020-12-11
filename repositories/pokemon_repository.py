from db.run_sql import run_sql

from models.pokemon import Pokemon

def save(pokemon):
    sql = "INSERT INTO pokemons (nickname, species, type, dob, trainer_name, trainer_number, status, nurse_id) VALUES (%s, %s, %s, %s, %s, %s, %s, %s) RETURNING *"
    values = [pokemon.nickname, pokemon.species, pokemon.type, pokemon.dob, pokemon.trainer_name, pokemon.trainer_number, pokemon.status, pokemon.nurse.id]
    results = run_sql(sql, values)
    id = results[0]['id']
    pokemon.id = id
    return pokemon

#delete_all
def delete_all():
    sql = "DELETE FROM pokemons"
    run_sql(sql)
#delete

def delete(id):
    sql = "DELETE FROM pokemons WHERE id = %s"
    values = [id]
    run_sql(sql, values)
#select_all
#select
#update