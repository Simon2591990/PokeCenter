import pdb

from models.nurse import Nurse
from models.pokemon import Pokemon
from models.trainer import Trainer
import repositories.nurse_repository as nurse_repository
import repositories.pokemon_repository as pokemon_repository
import repositories.trainer_repository as trainer_repository

# pokemon_repository.delete_all()
# nurse_repository.delete_all()
# trainer_repository.delete_all()



nurse_1 = Nurse("Joy", "Fire")
nurse_repository.save(nurse_1)
trainer = Trainer("Simon", 12345)
trainer_repository.save(trainer)


pokemon = Pokemon('Seed Backman', 'Bulbasaur', 'Grass', '25/09/1990', trainer , 'burned')

pokemon.assign_nurse(nurse_1)
pokemon_repository.save(pokemon)

trainer.name = 'Simondovich'



trainer_repository.update(trainer)

nurse_1.name = "Betsy"

nurse_repository.update(nurse_1)