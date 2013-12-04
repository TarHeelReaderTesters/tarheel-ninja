import Image
import ImageChops
import math, operator
import sys
import unittest



def compareMacSafari(pages):
    result = ''
    for p in pages:
        f1 = 'images/base/MAC/safari/' + p
        f2 = 'images/new/MAC/firefox/' + p
        result += (compare(f1,f2))
        if result == 'Unable to compute image difference':
            print result
            break
    runMessage(f1,f2,result,pages)

def compareMacFirefox(pages):
    result = ''
    for p in pages:
        f1 = 'images/base/MAC/firefox/' + p
        f2 = 'images/new/MAC/firefox/' + p
        result += (compare(f1,f2))
        if result == 'Unable to compute image difference':
            print result
            break
    runMessage(f1,f2,result,pages)

def compareWindowFirefox(pages):
    result = ''
    for p in pages:
        f1 = 'images/base/WINDOWS/firefox/' + p
        f2 = 'images/new/WINDOWS/firefox/' + p
        result += (compare(f1,f2))
        if result == 'Unable to compute image difference':
            print result
            break
    runMessage(f1,f2,result,pages)

def compareWindowChrome(pages):
    result = ''
    for p in pages:
        f1 = 'images/base/WINDOWS/chrome/' + p
        f2 = 'images/new/WINDOWS/chrome/' + p
        result += (compare(f1,f2))
        if result == 'Unable to compute image difference':
            print result
            break
    runMessage(f1,f2,result,pages)

def compareWindowIE10(pages):
    result = ''
    for p in pages:
        f1 = 'images/base/WINDOWS/iexplore10/' + p
        f2 = 'images/new/WINDOWS/iexplore10/' + p
        result += (compare(f1,f2))
        if result == 'Unable to compute image difference':
            print result
            break
    runMessage(f1,f2,result,pages)

def compareWindowIE8(pages):
    result = ''
    for p in pages:
        f1 = 'images/base/WINDOWS/iexplore8/' + p
        f2 = 'images/new/WINDOWS/iexplore8/' + p
        result += (compare(f1,f2))
        if result == 'Unable to compute image difference':
            print result
            break
    runMessage(f1,f2,result,pages)




def runMessage(file1, file2, string, name):
    if string == '11111':
        print 'passed'
    else:
        count = 0
        for c in string:
            if c == '0':
                print 'failed' + ' ' + file1 + ' ' + file2 + ' ' + name[count]
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

class imageComparison(unittest.TestCase):

    def setUp(self):
        self.name = ['page2.png', 'page3.png', 'page4.png', 'page5_japanese.png', 'title.png']

    def test_compareMacSafari(self):
        compareMacSafari(self.name)

    def test_compareWindowFirefox(self):
        compareWindowFirefox(self.name)

    def test_compareWindowChrome(self):
        compareWindowChrome(self.name)

    def test_compareWindowIE10(self):
        compareWindowIE10(self.name)

    def test_compareWindowIE8(self):
        compareWindowIE8(self.name)


if __name__== '__main__':
        unittest.main()