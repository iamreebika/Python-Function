array_nums1 = [22,12,3,4,23,11,44,]
array_nums2 = [9,4,55,66,7]
print("Original arrays:")
print(array_nums1)
print(array_nums2)
result = list(filter(lambda x: x in array_nums1, array_nums2))
print ("\nIntersection of the said arrays: ",result)

