import os
count=0
cmd=input("Enter what do you want: ")
cmd_list=cmd.strip().split()
print(cmd_list)
rm_words=[]
stopwords=["run","open","hey","there","would","you"]
for i in stopwords:
    if i in cmd_list:
        cmd_list.remove(i)
app=' '.join(cmd_list)
val=os.system('sudo dpkg --get-selections | sed "s/.*deinstall//" | sed "s/install$//g" > pkglist.txt')

with open("pkglist.txt", encoding="utf-8") as file:
    x = [l.strip() for l in file]
    # print("aaaa")
for i in cmd_list:
    if i in x:
        os.system(i)
        count=1
if count==1:
    print("here you go!!")
else:
    print("Software not installed")
