#!/usr/bin/env python3


def compute(base, value):
    base = list(base)
    base.append(value)
    result = sum(base)
    print(result)
if __name__ == '__main__':
    testlist = (10, 20, 30)  
    compute(testlist, 15)
    compute(testlist, 25)
    compute(testlist, 35)
    '''
    bug is testlist = [10, 20, 30]
    when function us this []
    because it will become another, so we
    can not use it,we use tuple because it
    will not change
    '''
