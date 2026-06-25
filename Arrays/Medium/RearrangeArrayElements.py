class RearrangeArrayElementBySign:
    def bruteforce(arr):
        n = len(arr) // 2
        pos = [] 
        neg = []
        posindex = 0
        negIndex = 1

        for i in arr:
            if i < 0:
                neg.append(i)
            else:
                pos.append(i)

        
        for i in pos:
            arr[posindex] = i
            posindex += 2

        for i in neg:
            arr[negIndex] = i
            negIndex += 2

    def optimal(arr):
        ans = [0] * len(arr)
        posIndex = 0
        negIndex = 1
        for i in arr:
            if i > 0:
                ans[posIndex] = i
                posIndex += 2
            else:
                ans[negIndex] = i
                negIndex+=2

    def secondVariety(arr): #When number of negatives and positives are not equal
        n = len(arr)
        pos = [] 
        neg = []

        for i in arr:
            if i < 0:
                neg.append(i)
            else:
                pos.append(i)

        
        if len(pos) > len(neg):
            for i in range(len(neg)):
                arr[2*i] = pos[i]
                arr[2*i+1] = neg[i]
            
            idx = len(neg) * 2
            for i in range(len(neg),len(pos)):
                arr[idx] = pos[i]
                idx+= 1
        else:
            for i in range(len(pos)):
                arr[2*i] = pos[i]
                arr[2*i+1] = neg[i]
            
            idx = len(pos) * 2
            for i in range(len(pos),len(neg)):
                arr[idx] = neg[i]
                idx+= 1

        

        print(arr)

        




arr = [3,1, -9,-2,-5,-2]
obj = RearrangeArrayElementBySign
obj.secondVariety(arr)
# print(arr)
