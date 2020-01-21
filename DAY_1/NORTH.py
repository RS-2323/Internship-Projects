import csv
import string
list1=[ ]
alpha=list(string.ascii_lowercase)+list(string.ascii_uppercase)
with open('ALL.csv','rt') as inf, open('inf', 'w') as outf:
    reader = csv.reader(inf)
    writer = csv.writer(outf)
    for i in reader:
        if i not in list1:
            if(i[4]=='North'):
                
                list1.append(i)
        else:
            continue
with open('NORTH.csv','wt') as file_1:
    
    write=csv.writer(file_1)
    if(csv.writer(file_1)>0):
        print "create sucessfully"
        write.writerows(list1)
    else:
        "not create"
    
                
       


            

 
