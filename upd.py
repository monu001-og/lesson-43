file1=open('Codingal.txt','r' )
file2=open('CodingalUpdated.txt','w')
#reading each line from original
#text file
for line in file1.readlines():
        if not(line.startswith('coding')):
               print(line)
               file2.write(line)
               
file2.close()
file1.close()

