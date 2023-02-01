from random import randint
num_rand = [randint(0, 100) for _ in range(10)]
num_seq = [num for num in range(10)]
num_sqrt = list(map(lambda i: i**0.5, num_rand))
num_sum = list(map(lambda x, y: round(x+y), num_rand, num_seq))
# map applies a function (lambda) to each element of the list (num_rand)

if __name__ == "__main__":
    print("Random", num_rand)
    print("Square root", num_sqrt)
    print("Sum", num_sum)
