def genrange(start_num, end_num):
    while start_num<=end_num:
        yield start_num
        start_num+=1


print(list(genrange(1, 10)))