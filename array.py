arr=[]
def create_array():
    size=int(input("enter the size of an array  "))
    for i in range(size):
        element=int(input("enter the elements  "))
        arr.append(element) 
    return arr
array=create_array()

print(f"the array is {array}")
 # type: ignore