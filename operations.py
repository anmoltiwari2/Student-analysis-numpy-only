#fucntions related to analysis of dataset
import numpy as np
def show_shape(data):
    print("dimensions opf dataset: ",data.shape)
    print("num of rows: ",data.shape[0])
    print("num of columns: : ",data.shape[1])

def show_size(data):
    print("size of dataset: ",data.size)

def show_firstelements(data):
    a=int(input("how many rows you wanna see: "))
    print("elements are:",data[:a])

def show_lastelements(data):
    a=int(input("enter last rows you want: "))
    print("elements are: ",data[-a:])

def show_rowelement(data):
    a=int(input("enter row you want: "))
    print("element is: ",data[a-1])

def show_totalgrades(data):
    g1=data[:,30].astype(int)
    g2=data[:,31].astype(int)
    g3=data[:,32].astype(int)
    print("sum of columns: ",np.sum(g1),np.sum(g2),np.sum(g3))
    print("average: ",np.mean(g1),np.mean(g2),np.mean(g3))

def show_student(data):
    try:
        a=int(input("enter number of record you wanna see: "))
        print("record: \n",data[a-1])
        b=int(input("enter column you want"))
        print("record: \n",data[a-1,b-1])
    except:
        print("index out of range enter choice and select same option again")

def find_topper(data):
    g3=data[:,32].astype(int)
    highest=np.max(g3)
    topper=data[g3==highest]
    print("highest scoree: \n",topper)

def find_lowest(data):
    g3=data[:,32].astype(int)
    lowest=np.min(g3)
    lowest=data[g3==lowest]
    print("lowest scorer: \n",lowest)

def find_passed(data):
    g1=data[:,30].astype(int)
    g2=data[:,31].astype(int)
    g3=data[:,32].astype(int)
    g4=g1+g2+g3
    passed=data[g4>30]
    for i in passed:
        print(i)


