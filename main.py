def print_factors(x):
    factors = []
    for i in range(1,x+1):
        if x%i == 0:
            factors.append(i)
    print(factors)

def factors():
    x = 52633
    factors = []
    for i in range(1,x+1):
        if x%i == 0:
            factors.append(i)
    print(factors)
def list_factors(l):
    factors = {}
    for x in l:
        factors[x] = []  # Initialize an empty list for each number in the list l
        for i in range(1, x + 1):
            if x % i == 0:
                factors[x].append(i)  # Append factors to the corresponding key
    print(factors)
    return factors

def main():
    l = [52633, 8137, 1024, 999]
    print("Hello World")
    factors()
    print_factors(4321)
    list_factors(l)
if __name__ == '__main__':
    main()