import unittest
from models.pokemon import Pokemon
from models.nurse import Nurse

class TestPokemon(unittest.TestCase):

    def setUp(self):
        self.pokemon = Pokemon("Seed Backman", "Bulbasaur", "Grass", "25/09/1990", "Ash", 259, 'burned' )

    def test_pokemon_has_nickname(self):
        self.assertEqual("Seed Backman", self.pokemon.nickname)

    def test_pokemon_has_species(self):
        self.assertEqual("Bulbasaur", self.pokemon.species)

    def test_pokemon_has_type(self):
        self.assertEqual("Grass", self.pokemon.type)

    def test_pokemon_has_dob(self):
        self.assertEqual("25/09/1990", self.pokemon.dob)

    def test_pokemon_has_trainer_name(self):
        self.assertEqual("Ash", self.pokemon.trainer_name) 

    def test_pokemon_has_trainer_number(self):
        self.assertEqual(259, self.pokemon.trainer_number)    

    def test_pokemon_has_status(self):
        self.assertEqual('burned', self.pokemon.status)

    def test_pokemon_before_nurse(self):
        self.assertEqual(None, self.pokemon.nurse) 

    def test_assign_nurse(self):
        nurse = Nurse('Joy')
        self.pokemon.assign_nurse(nurse)
        self.assertEqual(nurse, self.pokemon.nurse)

    def test_get_nurse_name(self):
        nurse = Nurse('Joy')
        self.pokemon.assign_nurse(nurse)
        self.assertEqual('Joy', self.pokemon.nurse.name)

    
