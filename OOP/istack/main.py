# TODO
class IntegerStack:
    def __init__(self, *, max_size: int = 10):
        self.items = []
        self.max_size = max_size

    def push(self, item: int) -> bool:
        if self.is_full():
            return False
        # Insert item at the beginning to maintain order for LIFO
        self.items.insert(0, item)
        return True

    def pop(self) -> int:
        if self.is_empty():
            raise IndexError("pop from empty stack")
        # Remove and return the top item
        return self.items.pop(0)

    def top(self) -> int:
        if self.is_empty():
            raise IndexError("top from empty stack")
        # Return the top item without removing it
        return self.items[0]

    def is_empty(self) -> bool:
        return len(self.items) == 0

    def is_full(self) -> bool:
        return len(self.items) >= self.max_size

    def expand(self, factor: int = 2) -> None:
        self.max_size *= factor

    def dump_to_file(self, path: str) -> None:
        with open(path, 'w') as file:
            file.write("\n".join(map(str, self.items)))

    @classmethod
    def load_from_file(cls, path: str) -> 'IntegerStack':
        stack = cls()
        with open(path, 'r') as file:
            for line in reversed(list(file)):
                item = int(line.strip())
                if stack.is_full():
                    stack.expand()
                stack.push(item)
        return stack

    def __getitem__(self, index: int) -> int:
        return self.items[index]

    def __setitem__(self, index: int, item: int) -> None:
        self.items[index] = item

    def __add__(self, other: 'IntegerStack') -> 'IntegerStack':
        # When adding two stacks, combine them in a way that retains the LIFO order for both.
        result = IntegerStack(max_size=self.max_size + other.max_size)
        result.items = list(reversed(self.items)) + list(reversed(other.items))
        result.items.reverse()  # Reverse the result to keep LIFO order.
        return result

    def __iter__(self) -> 'IntegerStackIterator':
        return IntegerStackIterator(self)

    def __len__(self) -> int:
        return len(self.items)

    def __str__(self) -> str:
        # Print the stack in LIFO order (top element first).
        return "\n".join(map(str, self.items))


class IntegerStackIterator:
    def __init__(self, stack: IntegerStack):
        self.stack = stack
        self.index = 0

    def __next__(self) -> int:
        if self.index >= len(self.stack.items):
            raise StopIteration
        value = self.stack.items[self.index]
        self.index += 1
        return value
