def user_selection(user_choice):
    while True:
        try:
            user_choice = int(input(user_choice))
        except ValueError:
            print("Invalid number")
            continue
        else:
            if user_choice == 1 or user_choice == 2 or user_choice == 3 or user_choice == 4:
                return user_choice
            else:
                print("Invalid selection")
                user_choice = user_choice


def menu_display():
    menu = user_selection("press 1 for Dog Attributes \nPress 2 for Subtraction \nPress 3 for Multiplication \nPress "
                          "4 for Division\n")
    return menu
