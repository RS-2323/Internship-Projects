import csv
import string
list1=[ ]
alpha=list(string.ascii_lowercase)+list(string.ascii_uppercase):
    reader = csv.reader(inf)
    writer = csv.writer(outf)
    list1.append(['DSL Id','Current RCA Value','Primary IP','DSL ID:RCA:IP','HUB','Circle'])
    for i in reader:
        if i not in list1:
            if(i[0][0] !='0' and i[0][0] not in alpha):
                i[0]='0'+str(i[0])
                list1.append(i)
            else:
                list1.append(i)
        else:
            continue
with open('ALL.csv','wt') as file_1:
    
    write=csv.writer(file_1)
    if(csv.writer(file_1)>0):
        print "create sucessfully"
        write.writerows(list1)
    else:
        "not create"
    
                
       


            

 
