import pdb

from models.nurse import Nurse
from models.pokemon import Pokemon
import repositories.nurse_repository as nurse_repository
import repositories.pokemon_repository as pokemon_repository

# pokemon_repository.delete_all()
# nurse_repository.delete_all()



nurse_1 = Nurse("Joy")

nurse_repository.save(nurse_1)

pokemon = Pokemon('Seed Backman', 'Bulbasaur', 'Grass', '25/09/1990', 'Ash', 259, 'burned')

pokemon.assign_nurse(nurse_1)
pokemon_repository.save(pokemon)


pokemon.nickname = "Almost Ivysaur"

pokemon_repository.update(pokemon)




