#Write a program which will remove duplicates from the array.

arr = ['Beyza', 'Emre', 'John', 'Emre', 'Mark', 'Beyza']
arr = set(arr)
arr = list(arr)
print(arr)
#-------Second way------------------------

remove_dups = []

for i in range(0, len(arr)):
        if arr[i] not in remove_dups:
            remove_dups.append(arr[i])
print(remove_dups)
#-------------Assignment 2-------------------------
#Write a program which finds the largest element in the array
arr = [3,5,7,8,9,14,24,105]

print(max(arr))
#-------------Assignment 3--------------------------------
 #Write a program which finds the smallest element in the array
print(min(arr))
# stringArr = ['beyza', 'cem', 'ramazan', 'ak', 'ghrmhffjhfd', 'yep']
# print(min(stringArr)) # returns ak in alphabetical order
#------------Assigment 4----------------------------------
#Write a program to display a pyramid
string = "*"

for i in range(1, 18 , 2):
    print('{:^50}'.format(i * string))
