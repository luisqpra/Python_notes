from random import randint

num_rand = [randint(0, 100) for _ in range(10)]
animals = ['conejo', 'pez', 'sapo', 'perro', 'gato', 'tigre']

greater = list(filter(lambda x: x > 50, num_rand))
letterO = list(filter(lambda x: 'o' in str.lower(x), animals))

if __name__ == "__main__":
    print("Random", num_rand)
    print("Greater than 50", greater)
    print("Animals", animals)
    print("Animals with 'o'", letterO)
