
list = [2,1,5,4, 3, 2, 2]
i = 1

while i < len(list):
    for j in range (i,0,-1):
      if list[j-1] < list[i]:
        list.pop(i-1) 
      else:
        i += 1
print("list", list)
print(len(list))



# list = [1, 2, 4,5, 3, 2, 2]
# i = 1
# while i < len(list):
#     if list[i - 1] < list[i]:
#         list[i] += list[i - 1] 
#         list.pop(i - 1) 
#     else:
#         i += 1
# print("list", list)

