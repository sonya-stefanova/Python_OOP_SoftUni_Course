def squares(end_num):
    # curr_num = 1
    #
    # while curr_num <= end_num:
    #     yield curr_num ** 2
    #     curr_num += 1
    return (x**2 for x in range(1, end_num+1))

print(list(squares(5)))