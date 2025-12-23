from typing import Generic, TypeVar, List, Optional

T = TypeVar('T')


class Queue(Generic[T]):
    """Очередь (FIFO) в ООП стиле"""

    def __init__(self) -> None:
        self._items: List[T] = []

    def enqueue(self, item: T) -> None:
        """Добавить элемент в очередь"""
        self._items.append(item)

    def dequeue(self) -> Optional[T]:
        """Удалить и вернуть первый элемент"""
        return self._items.pop(0) if self._items else None

    def is_empty(self) -> bool:
        """Проверить пустоту очереди"""
        return len(self._items) == 0

    def size(self) -> int:
        """Вернуть размер очереди"""
        return len(self._items)

    def __str__(self) -> str:
        return f"Queue({self._items})"


class Stack(Generic[T]):
    """Стек (LIFO) в ООП стиле"""

    def __init__(self) -> None:
        self._items: List[T] = []

    def push(self, item: T) -> None:
        """Добавить элемент в стек"""
        self._items.append(item)

    def pop(self) -> Optional[T]:
        """Удалить и вернуть верхний элемент"""
        return self._items.pop() if self._items else None

    def is_empty(self) -> bool:
        """Проверить пустоту стека"""
        return len(self._items) == 0

    def size(self) -> int:
        """Вернуть размер стека"""
        return len(self._items)

    def __str__(self) -> str:
        return f"Stack({self._items})"


# Демонстрация работы
if __name__ == "__main__":
    print("=== ООП реализация ===")

    # Тестирование Queue
    print("\n--- Queue ---")
    queue = Queue[int]()
    print(f"Создана пустая очередь: {queue}")
    print(f"Очередь пуста? {queue.is_empty()}")

    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    print(f"После добавления 1, 2, 3: {queue}")
    print(f"Размер очереди: {queue.size()}")

    item1 = queue.dequeue()
    print(f"Извлеченный элемент: {item1}")
    print(f"Очередь после dequeue: {queue}")

    item2 = queue.dequeue()
    print(f"Извлеченный элемент: {item2}")
    print(f"Очередь после dequeue: {queue}")

    # Тестирование Stack
    print("\n--- Stack (Стек) ---")
    stack = Stack[str]()
    print(f"Создан пустой стек: {stack}")
    print(f"Стек пуст? {stack.is_empty()}")

    stack.push("first")
    stack.push("second")
    stack.push("third")
    print(f"После добавления 'first', 'second', 'third': {stack}")
    print(f"Размер стека: {stack.size()}")

    popped1 = stack.pop()
    print(f"Извлеченный элемент: {popped1}")
    print(f"Стек после pop: {stack}")

    popped2 = stack.pop()
    print(f"Извлеченный элемент: {popped2}")
    print(f"Стек после pop: {stack}")

