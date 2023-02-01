from random import randint
from functools import reduce

num_rand = [randint(0, 100) for _ in range(10)]

result = reduce(lambda counter, x: (x+counter)/counter, num_rand)

if __name__ == "__main__":
    print("Random", num_rand)
    print("Result", result)
