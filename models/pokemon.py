class Pokemon:

    def __init__(self, nickname, species, type, dob, trainer_name, trainer_number, status, id = None):
        self.nickname = nickname
        self.species = species
        self.type = type
        self.dob = dob
        self.trainer_name = trainer_name
        self.trainer_number = trainer_number
        self.status = status
        self.id = id
        self.nurse = None

    def assign_nurse(self, nurse):
        self.nurse = nurse
        
