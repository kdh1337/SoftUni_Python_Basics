n = int(input())

for i in range(1111, 9999):
    str_n = str(i)
    total_4 = 0

    for j in str_n:
        if int(j) != 0:
            if n % int(j) == 0:
                total_4 += 1
            if total_4 == 4:
                print(i, end=' ')