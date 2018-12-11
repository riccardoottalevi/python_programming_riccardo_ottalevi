
>>> def a(a,b,c,d,e,f,g,h,i,l):
...     v=(a+b+c+d+e+f+g+h+i+l)/10
...     return v
... 
>>> a(5,5,5,5,5,5,5,5,5,5)
5.0


>>>L=[21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39]
>>> [L[i] for i in (1,3,5,7,9,11,13,15,17)]
[22, 24, 26, 28, 30, 32, 34, 36, 38]

>>>[L[i] for i in (0,3,6,9,12,15,18)]
[21, 24, 27, 30, 33, 36, 39]

>>> L[17:19]
[38, 39]


>>> for i in [2]:
...     for j in [4,6]:
...             print(i,j)
... 
2 4
2 6




L = ['1', '2', '3']:
	for i in range(10):
    		if i in L:
			print(i is in the list)
    		else:
    			print(i not found)



>>> f=open('Documents/python programming/exercise/fasta file','r')
>>> f
<_io.TextIOWrapper name='Documents/python programming/exercise/fasta file' mode='r' encoding='UTF-8'>
>>> read_first_line=f.readline()
>>> read_first_line
'sp|P24928|RPB1_HUMAN DNA-directed RNA polymerase II subunit RPB1 OS=Homo sapiens GN=POLR2A PE=1 SV=2\n'

>>> read_first_line.split('OS=')
['sp|P24928|RPB1_HUMAN DNA-directed RNA polymerase II subunit RPB1 ', 'Homo sapiens GN=POLR2A PE=1 SV=2\n']
>>> read_first_line[67:105]
'=Homo sapiens GN=POLR2A PE=1 SV=2\n'

 >>> read_first_line[67:105].split(' ')
['=Homo', 'sapiens', 'GN=POLR2A', 'PE=1', 'SV=2\n']
>>> ' '.join(str(x) for x in read_first_line[67:105].split(' '))
'=Homo sapiens GN=POLR2A PE=1 SV=2\n'





>>> c='asor rosa'
>>> c
'asor rosa'
>>> c[::-1]
'asor rosa'

>>> L=[1,7,3,9]
>>> L.sort()
>>> L
[1, 3, 7, 9]

>>> L=[1,7,3,9]
>>> Z = L[:]
>>> Z
[1, 7, 3, 9]
>>> L
[1, 7, 3, 9]
>>> Z.sort()
>>>L
[1,7,3,9]
>>>Z
[1,3,7,9]




>>> f=open('Documents/python programming/exercise/fasta file','r')
>>> f
<_io.TextIOWrapper name='Documents/python programming/exercise/fasta file' mode='r' encoding='UTF-8'>
>>> for line in f:
...	print(line)
...







































