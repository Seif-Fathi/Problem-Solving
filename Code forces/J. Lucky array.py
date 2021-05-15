if __name__ == '__main__':
    input()
    array = input().split()
    new_array = []
    for i in array:
        new_array.append(int(i))
    min_num = min(new_array)
    dic = {}
    for i in new_array:
        if str(i) not in dic:
            dic[str(i)] = 1
        else:
            dic[str(i)] +=1
    if dic[str(min_num)] %2 == 0:
        print('Unlucky')
    else:
        print('Lucky')
