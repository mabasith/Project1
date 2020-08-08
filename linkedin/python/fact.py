#!/usr/bin/env python3

def get_prime_factors(N):
    factors = list()
    divisor = 2
    while(divisor <= N):
        if ((N % divisor) == 0):
            factors.append(divisor)
            N = N / divisor
        else:
            divisor += 1
    return factors
    
def main():
    print(get_prime_factors(17))
if __name__ == "__main__":
    main()