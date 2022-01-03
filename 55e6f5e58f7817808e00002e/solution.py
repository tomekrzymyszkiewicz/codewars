def seven(m):
    division_counter = 0
    while len(str(m)) >= 3:
        m = m//10 - 2*(m%10)
        division_counter += 1
    return (m,division_counter)