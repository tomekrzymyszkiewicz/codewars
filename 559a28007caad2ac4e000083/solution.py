def perimeter(n):
    numbers = [1,1]
    for num in range(n-1):
        numbers.append(numbers[-1]+numbers[-2])
    return sum(numbers)*4