# E S C O M  -  I P N
# D A A D
# 4AV1
# Oct 15°, 2024
# @autor: Miguel Alexander Sanchez García
# TODO
class IntegerQueue:
    def __init__(self, *, max_size: int = 10):
        self.items = []
        self.max_size = max_size

    def enqueue(self, item: int) -> bool:
        if self.is_full():
            return False
        self.items.append(item)
        return True

    def dequeue(self) -> int:
        if self.is_empty():
            raise IndexError("dequeue from empty queue")
        return self.items.pop(0)

    def head(self) -> int:
        if self.is_empty():
            raise IndexError("head from empty queue")
        return self.items[0]

    def is_empty(self) -> bool:
        return len(self.items) == 0

    def is_full(self) -> bool:
        return len(self.items) >= self.max_size

    def expand(self, factor: int = 2) -> None:
        self.max_size *= factor

    def dump_to_file(self, path: str) -> None:
        with open(path, 'w') as file:
            file.write(",".join(map(str, self.items)))

    @classmethod
    def load_from_file(cls, path: str) -> 'IntegerQueue':
        queue = cls()
        with open(path, 'r') as file:
            line = file.readline().strip()
            if line:
                items = map(int, line.split(","))
                for item in items:
                    if queue.is_full():
                        queue.expand()
                    queue.enqueue(item)
        return queue

    def __getitem__(self, index: int) -> int:
        return self.items[index]

    def __setitem__(self, index: int, item: int) -> None:
        self.items[index] = item

    def __add__(self, other: 'IntegerQueue') -> 'IntegerQueue':
        result = IntegerQueue(max_size=self.max_size + other.max_size)
        result.items = self.items + other.items
        return result

    def __iter__(self) -> 'IntegerQueueIterator':
        return IntegerQueueIterator(self)

    def __len__(self) -> int:
        return len(self.items)

    def __str__(self) -> str:
        return ",".join(map(str, self.items))


class IntegerQueueIterator:
    def __init__(self, queue: IntegerQueue):
        self.queue = queue
        self.index = 0

    def __next__(self) -> int:
        if self.index >= len(self.queue.items):
            raise StopIteration
        value = self.queue.items[self.index]
        self.index += 1
        return value

    def __iter__(self):
        return self

# Developed by MASG
