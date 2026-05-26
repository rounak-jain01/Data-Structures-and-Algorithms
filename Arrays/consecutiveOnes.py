class MaximumConsecutiveOnes:
    def bruteForce(arr):
        n = len(arr)
        count = 0
        count_sum = 0
        for i in range(0,n):
            if arr[i] == 1:
                count += 1
                count_sum = max(count_sum, count)
                

            else:
                count = 0
        
        print(count_sum)

obj = MaximumConsecutiveOnes
arr = [1,1,0,0,1,1,1,0,1]
obj.bruteForce(arr)

        