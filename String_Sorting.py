def bubble_sort(strlist):
    length=len(strlist)
    
    for j in range(0,length-1):
        for i in range(0,length-j-1):
            if(len(strlist[i])>len(strlist[i+1])):
                strlist[i], strlist[i+1]=strlist[i+1], strlist[i]
            
    return strlist

file=input()

with open(file,'r') as f:
    lines=f.read().split('\n')
    
lines_sorted=bubble_sort(lines)
print(lines_sorted)