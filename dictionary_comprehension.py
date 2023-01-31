# Generate a dictionary in a single line of code
ani = ['conejo', 'pez', 'sapo', 'perro', 'gato', 'tigre']
nums = [nums+1 for nums in range(len(ani))]
nw_dic = {nums[i]: ani[i] for i in range(len(ani))}
nwdic_O = {nums[i]: ani[i] for i in range(len(ani)) if 'o' in ani[i]}

if __name__ == "__main__":
    print("Dictionary\n\t", nw_dic)
    print("Animals with 'o'\n\t", nwdic_O)
