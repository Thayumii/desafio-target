def inverter_string(s):
# Converte a string em lista.
    lista = list(s)
# Inicializa dois ponteiros, um no inicío e outro no final da lista.
    inicio = 0
    fim = len(lista) - 1

    while inicio < fim:
        lista[inicio], lista[fim] = lista[fim], lista[inicio]
        inicio += 1
        fim -= 1

# Converter a lista de volta para a string.
    return ''.join(lista)

# Solicita uma string ao usuário.
entrada = input("Digite a string que você deseja inverter: ")
string_invertida = inverter_string(entrada)

print(f"String invertida: {string_invertida}")