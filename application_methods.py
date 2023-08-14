from dog import Dog
from person import Person


class Methods:
    def dog_attributes(self, dog):
        print("I'm a", dog.firstAttribute)
        print("I'm a", dog.secondAttribute)

    def person_info(self, person):
        print("Hello my name is " + person.name + " and I" +
              " work at " + person.company + ".")
