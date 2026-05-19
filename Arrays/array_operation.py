class Insertion:
    def insertLast(arr,value):
        arr.append(value)


    def insertstart(arr,value):
        arr.append(0)
        for i in range(len(arr)-1,0,-1):
            arr[i] = arr[i-1]
        arr[0] = value

    def insertany(arr,value,idx = 2):
        arr.append(0)
        for i in range(len(arr)-1,idx-1,-1):
            arr[i] = arr[i-1]
        arr[idx] = value


class Deletion:
    def deletionend(arr):
        arr.pop()

    def deletionstart(arr):
        for i in range(len(arr)-1):
            arr[i] = arr[i+1]
        arr.pop()

    def deletionany(arr,idx):
        for i in range(idx,len(arr)-1):
            arr[i] = arr[i+1]
        arr.pop()


insert = Insertion
delete = Deletion
arr = [1,2,3,4,6,7,8,9]
# insert.insertstart(arr,value=45)
delete.deletionany(arr, 3)
print(arr)