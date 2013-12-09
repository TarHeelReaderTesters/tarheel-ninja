import Image
import ImageChops
import math, operator
import sys
import unittest



def compareMacSafari(pages,url):
    result = ''
    for p in pages:
        f1 = 'images/'+url+'/base/MAC/safari/' + p
        f2 = 'images/'+url+'/new/MAC/safari/' + p
        result += (compare(f1,f2))
        if result == 'Unable to compute image difference':
            print result
            break
    runMessage(f1,f2,result,pages)

def compareMacFirefox(pages,url):
    result = ''
    for p in pages:
        f1 = 'images/'+url+'/base/MAC/firefox/' + p
        f2 = 'images/'+url+'/new/MAC/firefox/' + p
        result += (compare(f1,f2))
        if result == 'Unable to compute image difference':
            print result
            break
    runMessage(f1,f2,result,pages)

def compareWindowFirefox(pages,url):
    result = ''
    for p in pages:
        f1 = 'images/'+url+'/base/WINDOWS/firefox/' + p
        f2 = 'images/'+url+'/new/WINDOWS/firefox/' + p
        result += (compare(f1,f2))
        if result == 'Unable to compute image difference':
            print result
            break
    runMessage(f1,f2,result,pages,url)

def compareWindowChrome(pages,url):
    result = ''
    for p in pages:
        f1 = 'images/'+url+'/base/WINDOWS/chrome/' + p
        f2 = 'images/'+url+'/new/WINDOWS/chrome/' + p
        result += (compare(f1,f2))
        if result == 'Unable to compute image difference':
            print result
            break
    runMessage(f1,f2,result,pages)

def compareWindowIE10(pages,url):
    result = ''
    for p in pages:
        f1 = 'images/'+url+'/base/WINDOWS/iexplore10/' + p
        f2 = 'images/'+url+'/new/WINDOWS/iexplore10/' + p
        result += (compare(f1,f2))
        if result == 'Unable to compute image difference':
            print result
            break
    runMessage(f1,f2,result,pages)

def compareWindowIE8(pages,url):
    result = ''
    for p in pages:
        f1 = 'images/'+url+'/base/WINDOWS/iexplore8/' + p
        f2 = 'images/'+url+'/new/WINDOWS/iexplore8/' + p
        result += (compare(f1,f2))
        if result == 'Unable to compute image difference':
            print result
            break
    runMessage(f1,f2,result,pages)




def runMessage(file1, file2, string, name):
    if string == '11111':
        return
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
        self.url = str(param[0])
        if self.url == "tarheelreader":
            self.name = ['page2.png', 'page3.png', 'page4.png', 'page5_japanese.png', 'title.png']
        else:
            self.name = ['page2.png', 'page3.png', 'page4.png', 'page5.png', 'page6.png', 'title.png']
    

    def test_compareMacSafari(self):
        compareMacSafari(self.name,self.url)
"""
    def test_compareWindowFirefox(self):
        compareWindowFirefox(self.name,self.url)

    def test_compareWindowChrome(self):
        compareWindowChrome(self.name,self.url)

    def test_compareWindowIE10(self):
        compareWindowIE10(self.name,self.url)

    def test_compareWindowIE8(self):
        compareWindowIE8(self.name,self.url)
"""

if __name__== '__main__':
        param=[]
        param.append(sys.argv[1])
        del sys.argv[1:]
        unittest.main()