import datetime as dt
import json
from typing import Dict, List, Any, Callable


class Person:
    def __init__(self, name: str, born_in: dt.datetime) -> None:
        self._name = name
        self._friends = []
        self._born_in = born_in

    def add_friend(self, friend: 'Person') -> None:
        self._friends.append(friend)
        friend._friends.append(self)

    @property
    def name(self) -> str:
        return self._name

    @property
    def born_in(self) -> dt.datetime:
        return self._born_in

    @property
    def friends(self) -> List['Person']:
        return self._friends.copy()


def encode_person_functional_private(obj: Person) -> bytes:
    """Функциональная сериализация с соблюдением инкапсуляции"""

    def collect_objects(current_obj, visited, objects):
        obj_id = id(current_obj)
        if obj_id in visited:
            return

        visited.add(obj_id)
        # Используем публичный интерфейс
        objects[obj_id] = {
            'name': current_obj.name,
            'born_in': current_obj.born_in.isoformat(),
            'friends': [id(friend) for friend in current_obj.friends]
        }

        for friend in current_obj.friends:
            collect_objects(friend, visited, objects)

    visited = set()
    objects = {}
    collect_objects(obj, visited, objects)

    data = {
        'objects': objects,
        'root_id': id(obj)
    }
    return json.dumps(data, indent=2).encode('utf-8')


def decode_person_functional_private(data: bytes) -> Person:
    """Функциональная десериализация с соблюдением инкапсуляции"""
    json_data = json.loads(data.decode('utf-8'))
    objects_data = json_data['objects']
    root_id = json_data['root_id']

    # Создаем все объекты сначала
    objects = {}
    for obj_id, obj_data in objects_data.items():
        born_in = dt.datetime.fromisoformat(obj_data['born_in'])
        person = Person(obj_data['name'], born_in)
        objects[obj_id] = person

    # Устанавливаем связи через публичный метод
    for obj_id, obj_data in objects_data.items():
        person = objects[obj_id]
        for friend_id in obj_data['friends']:
            friend = objects[str(friend_id)]
            # Используем add_friend для правильного установления связей
            if friend not in person.friends:  # Проверяем через публичный метод
                person.add_friend(friend)

    return objects[str(root_id)]

if __name__ == "__main__":
    p1 = Person("Ivan", dt.datetime(2020, 4, 12))
    p2 = Person("Petr", dt.datetime(2021, 9, 27))
    p1.add_friend(p2)

    encoded = encode_person_functional_private(p1)
    recreated_p1 = decode_person_functional_private(encoded)

    print("Функциональный без нарушения инкапсуляции:")
    print(f"Имя: {recreated_p1.name}")
    print(f"Друзей: {len(recreated_p1.friends)}")
    print(f"Имя друга: {recreated_p1.friends[0].name}")

