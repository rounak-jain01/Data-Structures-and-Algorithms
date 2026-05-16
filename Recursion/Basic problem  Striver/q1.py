# # Print Name 5 Times

# def print_name(cnt):
#     if cnt == 5:
#         return
#     cnt += 1
#     print("Rounak")
#     print_name(cnt)

# cnt = 0
# print_name(cnt)

'''Second Approach'''

def print_name(i,n):
    if i > n:
        return
    print("Rounak Jain")
    # i += 1
    print_name(i+1,n)

print_name(1,5)