class Pokemon:

    def __init__(self, nickname, species, type, dob, trainer, status, id = None):
        self.nickname = nickname
        self.species = species
        self.type = type
        self.dob = dob
        self.trainer = trainer
        self.status = status
        self.id = id
        self.nurse = None

    def assign_nurse(self, nurse):
        self.nurse = nurse
        
