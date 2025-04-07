from functools import lru_cache

class FibonacciIterator:
    def __init__(self, max_n):
        self.max_n = max_n
        self.a, self.b = 0, 1
        self.index = 0
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.index >= self.max_n:
            raise StopIteration
        self.a, self.b = self.b, self.a + self.b
        self.index += 1
        return self.a

@lru_cache(maxsize=None)
def fibonacci(n):
    if n < 0:
        raise ValueError("Index cannot be negative.")
    if n in {0, 1}:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

def fibonacci_generator(limit):
    a, b = 0, 1
    for _ in range(limit):
        yield a
        a, b = b, a + b

# Example Usage
if __name__ == "__main__":
    print("Fibonacci using Iterator:")
    for num in FibonacciIterator(10):
        print(num, end=" ")
    
    print("\nFibonacci using Generator:")
    for num in fibonacci_generator(10):
        print(num, end=" ")
    
    print("\nFibonacci using Memoization:")
    for i in range(10):
        print(fibonacci(i), end=" ")
