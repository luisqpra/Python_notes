from random import randint
# Generate a dictionary in a single line of code
ani = ['conejo', 'pez', 'sapo', 'perro', 'gato', 'tigre']
countries = ['col', 'arg', 'mex', 'ven', 'bra']
nums = [nums+1 for nums in range(len(ani))]
nw_dic = {nums[i]: ani[i] for i in range(len(ani))}
nwdic_O = {nums[i]: ani[i] for i in range(len(ani)) if 'o' in ani[i]}
population = {countries[i]: randint(1, 100) for i in range(len(countries))}

if __name__ == "__main__":
    print("Dictionary\n\t", nw_dic)
    print("Animals with 'o'\n\t", nwdic_O)
    print("Population\n\t", population)
