o = open('output.txt', 'wb')

fh = open('a.txt', 'rb')
fh2 = open('c.txt', 'rb')

for line in fh.readlines():
    o.write(line.strip('\r\n') + ' ' + fh2.readline().strip('\r\n') + '\n')

## If you want to write remaining files from input2.txt:
# for line in fh2.readlines():
#     o.write(line.rstrip('\r\n') + '\n')

fh.close()
fh2.close()
o.close()
