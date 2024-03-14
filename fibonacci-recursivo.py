'''
Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor sempre será a soma dos
 2 valores anteriores (exemplo: 0, 1,1,2, 3,5,8,13,21,34...), escreva um programa na linguagem que
desejar onde, informado um número, ele calcule a sequência de Fibonacci e retorne uma mensagem 
avisando se o número informado pertence ou não a sequência.

IMPORTANTE:
Esse número pode ser informado através de qualquer entrada de sua preferência ou pode ser previamente definida no código;
'''


def fibonacci(number: int):
    if number == 0:
        return 0
    elif number == 1:
        return 1
    else:
        return fibonacci(number-1) + fibonacci(number-2)


def create_fibonacci_list(number: int):
    fib_list = [0, 1]
    for i in range(2, number):
        num = fibonacci(i)
        fib_list.append(fibonacci(i))
        if num >= number:
            break
    return fib_list


def search_number_in_fibonacci_list(number: int, fibonacci_list: list):
    if int(number) in fibonacci_list:
        return (f'O numero {number} pertence a sequencia de fibonacci!!!')
    else:
        return (f'O numero {number} não pertence a sequencia de fibonacci')


def main():
    number = input(
        'digite um numero para procurar na sequencia de fibonacci: ')

    fibonacci_list = create_fibonacci_list(int(number))
    print('~'*30)
    print(f'Lista de fibonacci: {fibonacci_list}')
    result = search_number_in_fibonacci_list(number, fibonacci_list)
    print(result)


if __name__ == '__main__':
    main()
