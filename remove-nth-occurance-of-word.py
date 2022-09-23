mylist=["trees","fruits","vegs","trees","animals","trees","birds"]
word="trees"
n=3

print("Initial list:",mylist)
count=0
for i in range(0,len(mylist)-1):
    if(mylist[i]==word):
        count=count+1
        if(count==n):
            del mylist[i]

print("Modified list:",mylist)            