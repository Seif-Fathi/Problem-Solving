# -*- coding: utf-8 -*-
if __name__ == '__main__':
    tst_css = int(input())
    for i in range(tst_css):
        num_lmnt = int(input())
        num_lst = input().split()
        new_lst = []
        for i in num_lst:
            new_lst.append(int(i))
        new_lst2 = []
        b =1
        for num in new_lst:
            b = new_lst.index(num)+1
            for i in range(0,num_lmnt):
                try :
                    if b <=num_lmnt:
                        new_lst2.append(num + new_lst[b] + (b+1)-(new_lst.index(num)+1))
                        b+=1
                except IndexError:
                    break
        print(min(new_lst2))