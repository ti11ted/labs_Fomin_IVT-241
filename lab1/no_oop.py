from typing import Generic, TypeVar, List, Optional, Tuple

T = TypeVar('T')


# Queue в функциональном стиле
def create_queue() -> List[T]:
    """Создать пустую очередь"""
    return []


def enqueue(queue: List[T], item: T) -> List[T]:
    """Добавить элемент в очередь и вернуть новую очередь"""
    new_queue = queue.copy()
    new_queue.append(item)
    return new_queue


def dequeue(queue: List[T]) -> Tuple[Optional[T], List[T]]:
    """Удалить и вернуть первый элемент + новую очередь"""
    if not queue:
        return None, queue
    item = queue[0]
    new_queue = queue[1:]
    return item, new_queue


def is_queue_empty(queue: List[T]) -> bool:
    """Проверить пустоту очереди"""
    return len(queue) == 0


def queue_size(queue: List[T]) -> int:
    """Вернуть размер очереди"""
    return len(queue)


# Stack в функциональном стиле
def create_stack() -> List[T]:
    """Создать пустой стек"""
    return []


def push(stack: List[T], item: T) -> List[T]:
    """Добавить элемент в стек и вернуть новый стек"""
    new_stack = stack.copy()
    new_stack.append(item)
    return new_stack


def pop(stack: List[T]) -> Tuple[Optional[T], List[T]]:
    """Удалить и вернуть верхний элемент + новый стек"""
    if not stack:
        return None, stack
    new_stack = stack.copy()
    item = new_stack.pop()
    return item, new_stack


def is_stack_empty(stack: List[T]) -> bool:
    """Проверить пустоту стека"""
    return len(stack) == 0


def stack_size(stack: List[T]) -> int:
    """Вернуть размер стека"""
    return len(stack)


# Демонстрация работы
if __name__ == "__main__":
    print("=== функциональная реализация ===")

    # Тестирование Queue
    print("\n--- Queue (Очередь) ---")
    q = create_queue()
    print(f"Создана пустая очередь: {q}")
    print(f"Очередь пуста? {is_queue_empty(q)}")

    q = enqueue(q, 10)
    q = enqueue(q, 20)
    q = enqueue(q, 30)
    print(f"После добавления 10, 20, 30: {q}")
    print(f"Размер очереди: {queue_size(q)}")

    item1, q = dequeue(q)
    print(f"Извлеченный элемент: {item1}")
    print(f"Очередь после dequeue: {q}")

    item2, q = dequeue(q)
    print(f"Извлеченный элемент: {item2}")
    print(f"Очередь после dequeue: {q}")

    # Тестирование Stack
    print("\n--- Stack (Стек) ---")
    s = create_stack()
    print(f"Создан пустой стек: {s}")
    print(f"Стек пуст? {is_stack_empty(s)}")

    s = push(s, "A")
    s = push(s, "B")
    s = push(s, "C")
    print(f"После добавления 'A', 'B', 'C': {s}")
    print(f"Размер стека: {stack_size(s)}")

    popped1, s = pop(s)
    print(f"Извлеченный элемент: {popped1}")
    print(f"Стек после pop: {s}")

    popped2, s = pop(s)
    print(f"Извлеченный элемент: {popped2}")
    print(f"Стек после pop: {s}")

