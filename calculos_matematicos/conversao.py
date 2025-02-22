def inteiro_para_romano(num):  # Primeira função
    if not isinstance(num, int) or num <= 0:
        return "Entrada inválida"

    romanos = {1: 'I', 4: 'IV', 5: 'V', 9: 'IX', 10: 'X', 40: 'XL', 50: 'L', 90: 'XC', 100: 'C', 400: 'XD', 500: 'D', 900: 'CM', 1000: 'M'}
    resultado = ''
    for valor, simbolo in sorted(romanos.items(), reverse=True):
        while num >= valor:
            resultado += simbolo
            num -= valor
    return resultado

def romano_para_inteiro(romano): # Segunda função
    romanos = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    resultado = 0
    i = 0
    while i < len(romano):
        atual = romanos[romano[i]]
        proximo = romanos[romano[i+1]] if i + 1 < len(romano) else 0
        if atual < proximo:
            resultado += proximo - atual
            i += 2
        else:
            resultado += atual
            i += 1
    return resultado