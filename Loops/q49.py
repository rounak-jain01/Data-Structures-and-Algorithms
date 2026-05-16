# Two Sum: list mein do aise numbers dhundo jinki sum = target. (Brute 
# force O(n²)) 


def two_sum(l,key):
    for i in range(0,len(l)-1):
        for j in range(i+1,len(l)):
            tsum = 0
            tsum = l[i] + l[j]
            if tsum == key:
                print(l[i],l[j])
            
l = [1,2,3,4,3,5,1,9,0,6]
key = 6
two_sum(l,key)