# -*- coding: utf-8 -*-
if __name__ == '__main__':
    num = int(input())
    
    years = num // 365
    months = (num-years*365)//30
    print(years,'years')
    print(months, 'months')
    print(num - (years*365+months* 30), 'days')

