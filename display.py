from menu import menu_display
from Application import user_actions


def run():
    selection = menu_display()
    user_actions(selection)

    print()
    menu_display()





