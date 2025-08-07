#
# Mas isso pode ser um grande problema
#
# Ao analisar nosso código sobre `Animal`, você já parou pra pensar que
# nem todo animal é igual? Um cachorro pode latir, mas um gato?
#
# Pra resolver isso, podemos deixar as coisas mais específicas usando herança.
# Assim, um cachorro continua sendo um `Animal`, mas pode fazer um som próprio.
# O mesmo vale pro gato.
#
# OBS.: Essa não é uma analogia perfeita, um peixe também é um animal, mas
# não faz som nenhum. A ideia aqui é só didática.
#
# Esse tipo de relação entre tipos é chamado de subtipagem nominal
# (ou "nominal subtyping").
#
# Regra importante:
# Se B é um subtipo de A, então B É UM A.
# Porém, o contrário não é verdadeiro:
# A NÃO É um subtipo de B.
#
# Isso acontece porque os subtipos são mais específicos que os tipos.
# Portanto, não seria seguro usar A onde é esperado um B.

from exemplo05 import Animal
from exemplo06 import get_animal_name
from utils import cyan_print, sep_print


class Dog(Animal):
    def make_sound(self) -> None:
        cyan_print(f"{self.name!r} faz au au")

    def run(self) -> None:
        cyan_print(f"{self.name!r} está correndo...")


class Cat(Animal):
    def make_sound(self) -> None:
        cyan_print(f"{self.name!r} faz miau")


class Car:
    name: str = "Car"


if __name__ == "__main__":
    # Para os type checkers:
    dog = Dog("Dog")  # dog É UM Animal
    cat = Cat("Cat")  # cat É UM Animal
    car = Car()  # car NÃO É um Animal

    sep_print()
    # Então abaixo função aceitaria qual tipo?
    get_animal_name(dog)  # Dog
    get_animal_name(cat)  # Cat
    # get_animal_name(car)  # Cat

    # Vamos falar
    dog.make_sound()
    cat.make_sound()
    # car.make_sound()

    sep_print()

    dog2: Animal
    dog2 = Dog("Dog2")
    dog2.run()

    sep_print()
