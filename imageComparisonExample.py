import Image
import ImageChops
import math, operator
import sys

if __name__=="__main__":
	if(len(sys.argv)!=3):
		print "Wrong number of parameters!"
		print "Format is: %s <image1> <image2>" % (sys.argv[0],)
		sys.exit(1)

	print "comparing images..."

	h1=Image.open(str(sys.argv[1])).histogram()
	h2=Image.open(str(sys.argv[2])).histogram()

	rms = math.sqrt(reduce(operator.add, map(lambda a,b: (a-b)**2, h1, h2))/len(h1))
	print rms
