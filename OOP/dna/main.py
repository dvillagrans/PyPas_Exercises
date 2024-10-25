# TODO
class DNA:
    def __init__(self, sequence: str):
        self.sequence = sequence.upper()

    def __len__(self) -> int:
        return len(self.sequence)

    def __str__(self) -> str:
        return self.sequence

    @property
    def adenines(self) -> int:
        return self.sequence.count('A')

    @property
    def cytosines(self) -> int:
        return self.sequence.count('C')

    @property
    def guanines(self) -> int:
        return self.sequence.count('G')

    @property
    def thymines(self) -> int:
        return self.sequence.count('T')

    def __add__(self, other: 'DNA') -> 'DNA':
        result = []
        for base1, base2 in zip(self.sequence, other.sequence):
            result.append(max(base1, base2))
        if len(self.sequence) > len(other.sequence):
            result.extend(self.sequence[len(other.sequence):])
        elif len(other.sequence) > len(self.sequence):
            result.extend(other.sequence[len(self.sequence):])
        return DNA(''.join(result))

    def stats(self) -> dict:
        total = len(self.sequence)
        return {
            'A': (self.adenines / total) * 100 if total > 0 else 0,
            'C': (self.cytosines / total) * 100 if total > 0 else 0,
            'G': (self.guanines / total) * 100 if total > 0 else 0,
            'T': (self.thymines / total) * 100 if total > 0 else 0,
        }

    def __mul__(self, other: 'DNA') -> 'DNA':
        result = [base1 for base1, base2 in zip(self.sequence, other.sequence) if base1 == base2]
        return DNA(''.join(result))

    @classmethod
    def build_from_file(cls, path: str) -> 'DNA':
        with open(path, 'r') as file:
            sequence = file.readline().strip()
        return cls(sequence)

    def dump_to_file(self, path: str) -> None:
        with open(path, 'w') as file:
            file.write(self.sequence)

    def __getitem__(self, index: int) -> str:
        return self.sequence[index]

    def __setitem__(self, index: int, base: str) -> None:
        if base.upper() not in 'ACGT':
            base = 'A'
        self.sequence = self.sequence[:index] + base.upper() + self.sequence[index + 1:]
