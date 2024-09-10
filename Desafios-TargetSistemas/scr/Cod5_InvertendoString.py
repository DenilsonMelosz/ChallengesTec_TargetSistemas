def inverter_string(s):
    myresult = ''
    
    for i in range(len(s) - 1, -1, -1):
        myresult += s[i]
    
    return myresult

def main():
    string_original = input("Digite aqui a string que deseja inverter: ")
    string_invertida = inverter_string(string_original)
    print(f"String original: {string_original}")
    print(f"String invertida: {string_invertida}")

if __name__ == '__main__':
    main()
