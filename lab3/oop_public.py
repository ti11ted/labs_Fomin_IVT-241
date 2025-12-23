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


class PersonEncoderOOPPublic:
    def encode(self, obj: Person) -> bytes:
        """Сериализация с прямым доступом к приватным атрибутам"""
        visited = {}
        objects = {}

        def collect_objects(current_obj):
            obj_id = id(current_obj)
            if obj_id in visited:
                return

            visited[obj_id] = True
            # Нарушаем инкапсуляцию - прямой доступ к _name, _born_in, _friends
            objects[obj_id] = {
                'name': current_obj._name,
                'born_in': current_obj._born_in.isoformat(),
                'friends': [id(friend) for friend in current_obj._friends]
            }

            for friend in current_obj._friends:
                collect_objects(friend)

        collect_objects(obj)

        data = {
            'objects': objects,
            'root_id': id(obj)
        }
        return json.dumps(data, indent=2).encode('utf-8')


class PersonDecoderOOPPublic:
    def decode(self, data: bytes) -> Person:
        """Десериализация с прямым доступом к приватным атрибутам"""
        json_data = json.loads(data.decode('utf-8'))
        objects_data = json_data['objects']
        root_id = json_data['root_id']

        # Создаем объекты (возможно без конструктора)
        objects = {}
        for obj_id, obj_data in objects_data.items():
            # Через конструктор + прямой доступ
            born_in = dt.datetime.fromisoformat(obj_data['born_in'])
            person = Person(obj_data['name'], born_in)
            objects[obj_id] = person

        # Восстанавливаем связи с прямым доступом
        for obj_id, obj_data in objects_data.items():
            person = objects[obj_id]
            person._friends = []  # Очищаем и заполняем напрямую
            for friend_id in obj_data['friends']:
                friend = objects[str(friend_id)]
                person._friends.append(friend)

        return objects[str(root_id)]

if __name__ == "__main__":
    p1 = Person("Ivan", dt.datetime(2020, 4, 12))
    p2 = Person("Petr", dt.datetime(2021, 9, 27))
    p1.add_friend(p2)

    encoder = PersonEncoderOOPPublic()
    decoder = PersonDecoderOOPPublic()

    encoded = encoder.encode(p1)
    recreated_p1 = decoder.decode(encoded)

    print("ООП с нарушением инкапсуляции:")
    print(f"Имя: {recreated_p1._name}")  # Прямой доступ к приватному атрибуту
    print(f"Друзей: {len(recreated_p1._friends)}")
    print(f"Имя друга: {recreated_p1._friends[0]._name}")

