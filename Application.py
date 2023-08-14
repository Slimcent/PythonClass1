from Operations import DogOperations


def user_actions(user_choice):
    methods = DogOperations()

    while True:
        if user_choice == 1:
            methods.get_dog_attributes()
            return
        elif user_choice == 2:
            methods.get_person()
            return
        elif user_choice == 3:

            return
        else:

            return


