from random import randint
# map applies a function (lambda) to each element of the list (num_rand)

num_rand = [randint(0, 100) for _ in range(10)]
num_seq = [num for num in range(10)]
num_sqrt = list(map(lambda i: round(1000*i**0.5)/1000, num_rand))
num_sum = list(map(lambda x, y: round(x+y), num_rand, num_seq))

items = [
    {'product': 'shirt', 'price': 120},
    {'product': 'pants', 'price': 160},
    {'product': 'jacket', 'price': 205}
]

prices = list(map(lambda item: item["price"], items))

new_items = list(map(lambda x: x | {'tax': x['price']*0.19}, items))

if __name__ == "__main__":
    print("Random", num_rand)
    print("Square root", num_sqrt)
    print("Sum", num_sum)
    print("item prices", prices)
    print("new items", new_items)
