def bubblesort(list):
    global var_name
    count = 0
    n=len(list)
    for i in range(n-1):
        for j in range(n-i-1):
            if list[j]>list[j+1]:
                list[j],list[j+1]=list[j+1],list[j]
                count+=1
    print(count)


list=[3,0,2,5,1,4]
bubblesort(list)
print(list)
