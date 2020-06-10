# Write a function called is_sorted that takes a list as a parameter and returns True if the list is
# sorted in ascending orderand False otherwise. You can assume (as a precondition) that the elements of the list
# can be compared with the relational operators <, >, etc.
# For example, is_sorted([1,2,2]) should return True and is_sorted(['b','a']) should return False.def is_sorted():

#
# def is_sorted(list1):
#     j=1
#     for i in list1:
#         print(i,list1[j])
#         if i >list1[j]:
#             return False
#         else:
#             #if we not give this,we will get list index out of range error
#             if(j<len(list1)-1):
#                j+=1
#     return True
#
# list1=[]
# list1=input("enter the list : ").split(" ")
# sort_Check=is_sorted(list1)
# if sort_Check:
#     print("Sorted")
# else:
#     print("Not Sorted")

list1=[1,4,3,2]
print(sorted(list1))