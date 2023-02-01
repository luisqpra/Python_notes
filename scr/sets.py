# Set
#   It is modifiable
#   It does not have order
#   It does not have repeating elements
set_countries_A = {
    'col',
    'mex',
    'ven',
    'bol',
    'arg',
    'bra',
    'uru',
    'par',
    'chi',
    'per'
    }

set_countries_B = {
    'usa',
    'uk',
    'ita',
    'fra',
    'esp',
    'ale',
    'ucr'
}

set_countries_C = {
    'rus',
    'chi',
    'mex',
    'usa',
    'ven'
}

set_countries_D = {
    'jap',
    'aus',
    'ind',
    'egi',
    'usa',
    'col'
}


if __name__ == "__main__":
    print('set A\t', set_countries_A)
    print('set B\t', set_countries_B)
    print('set C\t', set_countries_C)
    print('set D\t', set_countries_D, '\n')
    # Add
    print('Add ', set_countries_D)
    set_countries_D.add('mal')
    print('\t', set_countries_D)
    # Update
    print('Update ', set_countries_C)
    set_countries_C.update({'kon', 'kos', 'col'})
    print('\t', set_countries_C)
    # Remove
    print('Remove ', set_countries_A)
    set_countries_A.remove('par')
    print('\t', set_countries_B)
    print('Discard ', set_countries_B)
    set_countries_B.discard('uk')
    print('\t', set_countries_B)
    # Clear
    set_temp = set_countries_A.copy()
    print('Clear ', set_temp)
    set_temp.clear()
    print('\t', set_temp)
    # Union
    print('Union ', set_countries_C, ' & ', set_countries_D)
    set_union_CD = set_countries_C.union(set_countries_D)
    #   set_countries_C | set_countries_D
    print('\t', set_union_CD)
    # Intersection
    print('Intersection ', set_countries_A, ' & ', set_countries_C)
    set_intersection_AC = set_countries_A.intersection(set_countries_C)
    #   set set_countries_A & set_countries_B
    print('\t', set_intersection_AC)
    # Difference
    print('Difference ', set_countries_D, ' & ', set_countries_A)
    set_difference_DA = set_countries_D.difference(set_countries_A)
    #   set set_countries_A - set_countries_B
    print('\t', set_difference_DA)
    # Symmetric Difference
    print('Symmetric_Difference ', set_countries_D, ' & ', set_countries_A)
    set_syDif_DA = set_countries_D.symmetric_difference(set_countries_A)
    #   set set_countries_A ^ set_countries_B
    print('\t', set_syDif_DA)
