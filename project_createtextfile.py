#whenever the user will say create text file the following function will be called
pc=0
def create():
    file=open('file%d.txt'%(pc+1),'w+')
    file.write(input())
create()
