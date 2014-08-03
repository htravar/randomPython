Python 2.7.8 (default, Jun 30 2014, 16:08:48) [MSC v.1500 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> randList = []
>>> def randomness():
	hi = 2.0
	lo = 1.0
	for i in range(10):
		x = random.uniform(lo, hi)
		randList.append(x)
	print randList

	
>>> def test(randList):
	count = 0
	for num in randList:
		if num < 1.5:
			count += 1
	print ("There are"), count, ("occurences of random floats less than 1.5")

	
>>> randomness()

Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    randomness()
  File "<pyshell#8>", line 5, in randomness
    x = random.uniform(lo, hi)
NameError: global name 'random' is not defined
>>> import random
>>> randomness()
[1.0005174440825892, 1.7121706024075078, 1.4994106730377612, 1.1664369228940363, 1.3718665715866791, 1.4344110248803488, 1.095883857142565, 1.3681379171528052, 1.1142634825631723, 1.7273365728260002]
>>> test(randList)
There are 8 occurences of random floats less than 1.5
>>> #don't forget import random!
