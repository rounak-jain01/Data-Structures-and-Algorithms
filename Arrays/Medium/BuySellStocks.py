class BuySellStock:
    def bruteforce(arr):
        n = len(arr)
        max_profit = 0

        for i in range(n):
            for j in range(i+1, n):
                profit = arr[j] - arr[i]
                max_profit = max(profit, max_profit)

        return max_profit
    
    def optimal(arr):
        min_price = arr[0]
        max_price = 0

        for i in arr:
            profit = i - min_price
            max_price = max(profit, max_price)
            min_price = min(i, min_price)

        return max_price


obj = BuySellStock
arr = [7,1,5,3,6,4]
print(obj.optimal(arr))