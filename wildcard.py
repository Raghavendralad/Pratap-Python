import sys
f = open('b.txt','r')
for mask in f.readlines():
 def wildcard_conversion(mask):
     wildcard = []
     for x in mask.split('.'):
         component = 255 - int(x)
         wildcard.append(str(component))
     wildcard = '.'.join(wildcard)
     return wildcard
 wildcard = wildcard_conversion(mask)

 ospf = (wildcard)
 print(ospf)
f.close()
