import Image
import ImageChops
import math, operator
import sys
import unittest

def compareSafari(pages):
    result = ''
    for p in pages:
        f1 = 'images/base/MAC/safari/' + p
        f2 = 'images/new/MAC/safari/' + p
        result += (compare(f1,f2))
        if result == 'Unable to compute image difference':
            print result
            break


    if result == '11111':
        print 'passed'
    else:
        count = 0
        for c in result:
            if c == '0':
                print 'failed' + ' ' + f1 + ' ' + f2 + ' ' + name[count]
            count += 1


def compare(file1, file2):
    h1=Image.open(file1).histogram()
    h2=Image.open(file2).histogram()
    try:
        rms = math.sqrt(reduce(operator.add, map(lambda a,b: (a-b)**2, h1, h2))/len(h1))
    except Exception:
        return 'Unable to compute image difference'
    if rms <= 25:
            return '1'
    else:
            return '0'


if __name__=="__main__":
    name = ['page2.png', 'page3.png', 'page4.png', 'page5_japanese.png', 'title.png']
    compareSafari(name)