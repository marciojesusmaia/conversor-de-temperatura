
from os import system, close
# CONVERSOR DE TEMPERATURAS

# FORMULAS
# C > K = C + 273,15
# C > F = (C * 1.8)+32
# K > C = K - 273,15
# K > F = K * 1.8 - 459.67
# F > K = (F + 459.67)*0.55
# F > C = (F - 32)/ 1.8

# FUNÇÕES DE CONVERSÃO
valor = 0
# CELSIUS PARA FARENHEIT
def c_to_f():
    # f = 0
    f = (valor * 1.8) + 32
    print(f)

# CELSIUS PARA KELVIN
def c_to_k():
    k = 0
    k = valor + 273.15
    print(k)

# KELVIN PARA CELSIUS
def k_to_c():
    c = 0
    c = valor - 273.15
    print(c)

# KELVIN PARA FARENHEIT
def k_to_f():
    f = 0
    f = valor * 1.8 - 459.67
    print(f)

# FARENHEIT PARA KELVIN
def f_to_k():
    k = 0
    k = (valor + 459.67) * 0.55
    print(k)

# FARENHEIT PARA CELSIUS
def f_to_c():
    c = 0
    c = (valor - 32) * 1.8
    print(c)

def conv_temp():
    

    print('-' * 40)
    print('* CONVERSOR DE TEMPERATURAS *'.ljust(40))
    print('-' * 40)
    print('1 - CELSIUS PARA KELVIN')
    print('2 - CELSIUS PARA FARENHEIT')
    print('3 - KELVIN PARA CELSIUS')
    print('4 - KELVIN PARA FARENHEIT')
    print('6 - FARENHEIT PARA CELSIUS')
    print('5 - FARENHEIT PARA KELVIN')
    print('0 - PARA SAIR DIGITE 0(ZERO)')
    print('-' * 40)
    print('')

if __name__ == '__main__':
    system('clear')

    while True:

        conv_temp()
        valor = float(input('Quanto deseja converter: '))


        escolha = input('Escolha a opção de conversão ou 0 para sair: ')
        
        if escolha == '1':
            c_to_f()
        elif escolha == '2':
            c_to_k()
        elif escolha == '3':
            k_to_c()
        elif escolha == '4':
            k_to_f()
        elif escolha == '5':
            f_to_k()
        elif escolha == '6':
            f_to_c()

        elif escolha == '0':
            exit()



