def inttooct(a):
    sayac = oct(a)
    return sayac[2:]


conversion_table = ['0', '1', '2', '3', '4', '5',
                    '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']


def decTohex(a):
    if(a <= 0):
        return ''
    remainder = a % 16
    return decTohex(a//16)+conversion_table[remainder]


def decTobin(a):
    sayac = bin(a)
    return sayac[2:]


def print_formatted(number):
    if(number >= 1 and number <= 99):
        i = 1
        while(i <= number):
            print(i, "", inttooct(i), "",
                  decTohex(i), "", decTobin(i))
            i += 1


if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
