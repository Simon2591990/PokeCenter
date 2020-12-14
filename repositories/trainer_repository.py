from db.run_sql import run_sql
import pdb

from models.trainer import Trainer

def save(trainer):
    sql = "INSERT INTO trainers (name, number) VALUES (%s, %s) RETURNING *"
    values = [trainer.name, trainer.number]
    results = run_sql(sql, values)
    id = results[0]['id']
    trainer.id = id
    return trainer

def select_all():
    trainers = []

    sql = "SELECT * FROM trainers"
    results = run_sql(sql)

    for row in results:
        trainer = Trainer(row['name'],row['number'], row['id'])
        trainers.append(trainer)
    return trainers

def select(id):
    trainer = None
    sql = "SELECT * FROM trainers WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]
    if result is not None:
        trainer = Trainer(result['name'], result['number'], result['id'])
    return trainer

def delete_all():
    sql = "DELETE FROM trainers"
    run_sql(sql)