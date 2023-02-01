def funtion_A(first_name: str, last_name: str) -> str:
    return first_name+' '+last_name


funtion_B = [lambda first_name, last_name: first_name+' '+last_name]

if __name__ == "__main__":
    full_name_A = funtion_A("Luis", "Quiroz")
    full_name_B = funtion_B[0]("Luis", "Quiroz")
    print(full_name_A)
    print(full_name_B)
