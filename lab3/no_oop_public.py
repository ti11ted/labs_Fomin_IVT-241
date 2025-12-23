import datetime as dt
import json
from typing import Dict, List, Any


class Person:
    def __init__(self, name: str, born_in: dt.datetime) -> None:
        self._name = name
        self._friends = []
        self._born_in = born_in

    def add_friend(self, friend: 'Person') -> None:
        self._friends.append(friend)
        friend._friends.append(self)


def encode_person_functional_public(obj: Person) -> bytes:
    """Функциональная сериализация с прямым доступом к данным"""

    def collect_objects(current_obj, visited, objects):
        obj_id = id(current_obj)
        if obj_id in visited:
            return

        visited.add(obj_id)
        # Прямой доступ к приватным атрибутам
        objects[obj_id] = {
            'name': current_obj._name,
            'born_in': current_obj._born_in.isoformat(),
            'friends': [id(friend) for friend in current_obj._friends]
        }

        for friend in current_obj._friends:
            collect_objects(friend, visited, objects)

    visited = set()
    objects = {}
    collect_objects(obj, visited, objects)

    data = {
        'objects': objects,
        'root_id': id(obj)
    }
    return json.dumps(data, indent=2).encode('utf-8')


def decode_person_functional_public(data: bytes) -> Person:
    """Функциональная десериализация с созданием объектов без конструктора"""
    json_data = json.loads(data.decode('utf-8'))
    objects_data = json_data['objects']
    root_id = json_data['root_id']

    # Создаем объекты без вызова конструктора
    objects = {}
    for obj_id, obj_data in objects_data.items():
        person = object.__new__(Person)
        person._name = obj_data['name']
        person._born_in = dt.datetime.fromisoformat(obj_data['born_in'])
        person._friends = []
        objects[obj_id] = person

    # Восстанавливание связей прямым доступом
    for obj_id, obj_data in objects_data.items():
        person = objects[obj_id]
        for friend_id in obj_data['friends']:
            friend = objects[str(friend_id)]
            person._friends.append(friend)

    return objects[str(root_id)]



if __name__ == "__main__":
    p1 = Person("Ivan", dt.datetime(2020, 4, 12))
    p2 = Person("Petr", dt.datetime(2021, 9, 27))
    p1.add_friend(p2)

    encoded = encode_person_functional_public(p1)
    recreated_p1 = decode_person_functional_public(encoded)

    print("Функциональный метод с нарушением инкапсуляции:")
    print(f"Имя: {recreated_p1._name}")  # Прямой доступ
    print(f"Друзей: {len(recreated_p1._friends)}")
    print(f"Имя друга: {recreated_p1._friends[0]._name}")

