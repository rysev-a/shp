from math import pow

def main():
    r1 = float(input())
    r2 = float(input())

    pi = 3.14

    s1 = pi * pow(r1, 2)
    s2 = pi * pow(r2, 2)

    print(s2 - s1)
    
if __name__ == '__main__':
    main()