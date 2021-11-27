import requests
from collections.abc import Iterator


class BasePokemon:
    def __init__(self, name: str):
        self.__name = name

    def __str__(self) -> str:
        return f'_______________ \n' \
               f'name: {self.__name} \n' \
               f'_______________'


class Pokemon(BasePokemon):
    def __init__(self, id: int, name: str, height: int, weight: int):
        super().__init__(name)
        self.__id = id
        self.__name = name
        self.__height = height
        self.__weight = weight

    @property
    def id(self) -> int:
        return self.__id

    @property
    def name(self) -> str:
        return self.__name

    @property
    def height(self) -> int:
        return self.__height

    @property
    def weight(self) -> int:
        return self.__weight

    def __str__(self) -> str:
        return f'_______________ \n' \
               f'Pokemon id: {self.__id} \n' \
               f'name: {self.__name} \n' \
               f'height: {self.__height} \n' \
               f'weight: {self.__weight} \n' \
               f'_______________'


class PokeAPI:

    @staticmethod
    def get_pokemon(name='', id=1) -> 'Pokemon':
        if name != '':
            result = requests.get(f'https://pokeapi.co/api/v2/pokemon/{name}').json()
        else:
            result = requests.get(f'https://pokeapi.co/api/v2/pokemon/{id}').json()

        info = [result['id'], result['name'], result['height'], result['weight']]

        return Pokemon(*info)

    @staticmethod
    def get_all(get_full=False) -> Iterator:
        counter = 0
        while counter <= 898:
            if not get_full:
                counter += 1
                yield PokeAPI.get_pokemon(id=counter)
            else:
                counter += 1
                result = requests.get(f'https://pokeapi.co/api/v2/pokemon/{counter}').json()
                yield BasePokemon(result['name'])


ditto = PokeAPI.get_pokemon(id=132)
print(ditto)
ditto = PokeAPI.get_pokemon('ditto')
print(ditto)

pokemon_list = []
pokemon_getter = PokeAPI.get_all()

for i in range(50):
    pokemon_list.append(next(pokemon_getter))

print(max(pokemon_list, key=lambda x: x.weight))
