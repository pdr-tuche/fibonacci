'''
 Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor sempre será a soma dos
 2 valores anteriores (exemplo: 0, 1,1,2, 3,5,8,13,21,34...), escreva um programa na linguagem que
desejar onde, informado um número, ele calcule a sequência de Fibonacci e retorne uma mensagem 
avisando se o número informado pertence ou não a sequência.

IMPORTANTE:
Esse número pode ser informado através de qualquer entrada de sua preferência ou pode ser previamente definida no código;
'''


def search_number_in_fibonacci(number: int):
    t1 = 0
    t2 = 1
    t3 = 0
    is_present = False

    fib_list = [t1, t2]
    while t3 < number:
        t3 = t1 + t2
        fib_list.append(t3)
        t1 = t2
        t2 = t3

    if number in fib_list:
        is_present = True

    return fib_list, is_present


def main():
    number = input(
        'digite um numero para procurar na sequencia de fibonacci: ')
    fibonnaci_list, is_present = search_number_in_fibonacci(int(number))

    print('~'*30)
    if is_present:
        print(f'O numero {number} pertence a sequencia de fibonacci!!!')
    else:
        print(f'O numero {number} não pertence a sequencia de fibonacci')
    print(f'Lista de fibonacci: {fibonnaci_list}')


if __name__ == '__main__':
    main()
