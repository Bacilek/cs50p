class Jar:
    def __init__(self, capacity=12):
        if not isinstance(capacity, int):
            raise ValueError(f"Error: {capacity} is not an integer.")
        if not capacity >= 0:
            raise ValueError(f"Error: {capacity} is not positive.")
        self._capacity = capacity
        self._size = 0

    def __str__(self):
        return "🍪" * self._size

    def deposit(self, n):
        if self._size + n > self._capacity:
            raise ValueError(f"Error: {self._size + n} (jar size + new deposit) is more than {self._capacity} (capacity).")
        self._size += n

    def withdraw(self, n):
        if self._size < n:
            raise ValueError(f"Error: {n} (cookie withdrawal) is more than {self._size} (jar size).")
        self._size -= n

    @property
    def capacity(self):
        return self._capacity

    @property
    def size(self):
        return self._size


def main():
    ...


if __name__ == "__main__":
    main()
