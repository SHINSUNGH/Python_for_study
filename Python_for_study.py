
# a = 300
# b = 300

# print (a is b)

# print (a == b)

# data_list = [1,2,3,4,5,[1,2,3]]
# print (data_list)
# print (len(data_list))
# print (len(data_list[-1]))

# print (min(data_list[-1]))
# print (max(data_list[-1]))

# print (count(data_list))

data_1 = [3,56,7,2,5,6]
data_1.sort()
print (data_1)

data_1.sort(reverse=True)
print (data_1)

data_1[0] = 10
print (data_1)

data_1 [1:3] = [2,2]
print (data_1)

data_1 [1:4] = [1,5,9,8,7,5,15]
data_1.sort()
del data_1 [:]
print (data_1)