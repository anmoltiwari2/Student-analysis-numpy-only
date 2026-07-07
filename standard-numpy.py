import numpy as np
import operations as op
data=np.genfromtxt("math.csv",delimiter=",",dtype="str",skip_header=1)
print(data)
op.find_passed(data)
print("ENTER FOR THE FOLLOWING OPERATIONS: ")
print("1. for shape\n2. for size\n3. for first rows\n4. for last rows\n5. for specific row")
print("6. for total grades\n7. for specific student\n8. for topper\n9. for lowest scorer\n10. for passed students")
while True:
    c=int(input("enter your choice"))
    if c==1:
        op.show_shape(data)
    elif c==2:
        op.show_size(data)
    elif c==3:
        op.show_firstelements(data)
    elif c==4:
        op.show_lastelements(data)
    elif c==5:
        op.show_rowelement(data)
    elif c==6:
        op.show_totalgrades(data)
    elif c==7:
        op.show_student(data)    
    elif c==8:
        op.find_topper(data)    
    elif c==9:
        op.find_lowest(data)
    elif c==10:
        op.find_passed(data)
    else:
        break