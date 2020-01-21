import csv
import string
list1=[ ]
alpha=list(string.ascii_lowercase)+list(string.ascii_uppercase)
with open('pranav_1111.csv','rt') as inf, open('inf', 'w') as outf:
    reader = csv.reader(inf)
    writer = csv.writer(outf)
    for i in reader:
        if i not in list1:
            if "ip description SSP" in i[1]:
                list1.append(i)
        else:
            print i[1]
            continue
with open('VTA.csv','wt') as file_1:
    
    write=csv.writer(file_1)
    if(csv.writer(file_1)>0):
        print "create sucessfully"
        write.writerows(list1)
    else:
        "not create"
    
                
       


            

 
