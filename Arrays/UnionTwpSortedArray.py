class UnionofTwoSortedArray:
    def bruteforce(arr1, arr2):
        m = len(arr1)
        n = len(arr2)
        s = set()

        for i in range(n):
            s.add(arr1[i])

        for i in range(n):
            s.add(arr2[i])
        
        union = []
        for i in s:
            union.append(i)

    def optimalApproach(arr1,arr2):
        union = []
        i = 0
        j = 0
        m = len(arr1)
        n = len(arr2)

        while i < m and j < n:
            if arr1[i] <= arr2[j]:
                if len(union) == 0 or union[-1] != arr1[i]:
                    union.append(arr1[i]) 
                i+=1
            else:
                if len(union) == 0 or union[-1] != arr2[j]:
                    union.append(arr2[j]) 
                j+=1 

        while i < m:
            if len(union) == 0 or union[-1] != arr1[i]:
                union.append(arr1[i]) 
            i+=1
        while j < n:
            if len(union) == 0 or union[-1] != arr2[j]:
                union.append(arr2[j]) 
            j+=1
            

        print(union)   
              


arr1 = [1,1,2,3,4,4,5,11]
arr2 = [2,2,3,4,5,6,7,8,9]
obj = UnionofTwoSortedArray
obj.optimalApproach(arr1,arr2)

