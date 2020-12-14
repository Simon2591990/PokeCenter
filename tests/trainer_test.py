import unittest

from models.trainer import Trainer

class TestTrainer(unittest.TestCase):

    def setUp(self):
        self.trainer = Trainer("Simon", 123456)

    def test_trainer_has_name(self):
        self.assertEqual("Simon", self.trainer.name)

    def test_trainer_has_number(self):
        self.assertEqual(123456, self.trainer.number)
