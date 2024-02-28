def move_to_last(mylist, element):
    print(mylist)
    size=len(mylist)
    index=mylist.index(element)
    #print(index)
    mylist.append(mylist.pop(index))
    print(mylist)
    while size > 2 and element in mylist:
        move_to_last(mylist[0:len(mylist)-1], element)


arr = [4,1,5,2,452,4,5,256,79]
#print(f'Initial array: {arr}')

print(arr.index(3))
#move_to_last(arr,4)
#print(f'Final array: {arr}')