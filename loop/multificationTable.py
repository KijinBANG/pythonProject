for i in range(1, 10):
    j=1
    while j <= 9:
        result = format(i*j, '2d')
        print('%d X %d = %s'%(j, i, result), end="\t\t")
        j += 1
    print()