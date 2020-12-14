from db.run_sql import run_sql
import pdb

from models.nurse import Nurse

def save(nurse):
    sql = "INSERT INTO nurses (name) VALUES (%s) RETURNING *"
    values = [nurse.name]
    results = run_sql(sql, values)
    id = results[0]['id']
    nurse.id = id
    return nurse

def select_all():
    nurses = []

    sql = "SELECT * FROM nurses"
    results = run_sql(sql)

    for row in results:
        nurse = Nurse(row['name'], row['id'])
        nurses.append(nurse)
    return nurses

def select(id):
    nurse = None
    sql = "SELECT * FROM nurses WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]
    
    if result is not None:
        nurse = Nurse(result['name'], result['id'])
    return nurse

def delete_all():
    sql = "DELETE FROM nurses"
    run_sql(sql)

def delete(id):
    sql = "DELETE FROM nurses WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def update(nurse):
    sql = "UPDATE nurses SET name = %s WHERE id = %s"
    values = [nurse.name, nurse.id]
    run_sql(sql, values)



