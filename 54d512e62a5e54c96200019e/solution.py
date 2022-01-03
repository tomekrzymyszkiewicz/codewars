def prime_factors(n):
    factors = {}
    while n != 1:
        divider = 2
        while n%divider != 0: divider += 1
        n /= divider    
        factors[divider] = factors[divider] + 1 if factors.get(divider) else 1
    return ''.join(f'({divider}**{quantity})' if quantity > 1 else f'({divider})' for divider,quantity in factors.items())
