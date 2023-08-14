from dog import Dog
from dog_methods import Methods


class DogOperations:
    def get_attributes(self):
        Rodger = Dog()
        print(Rodger.firstAttribute)

        # Create an instance of the Methods class
        methods_instance = Methods()
        methods_instance.dog_attributes(Rodger)
