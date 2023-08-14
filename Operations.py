from dog import Dog
from person import Person
from application_methods import Methods


class DogOperations:
    methods_instance = Methods()

    def get_dog_attributes(self):
        Rodger = Dog()
        print(Rodger.firstAttribute)

        self.methods_instance.dog_attributes(Rodger)

    def get_person(self):
        Obi = Person("Obinna", "Tenece")

        self.methods_instance.person_info(Obi)
