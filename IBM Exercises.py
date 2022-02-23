


#n =int(input('Enter The Integer ')) # Enter an int value for n before running the program

#for i in range(n):
#    if n - i:
#        print((n>0)*"*")


print('Practice Iteration -For Loop')

print('Demonstrate your knowledge and understanding of Python’s list comprehension syntax by iterating through a range collection to produce the following lists.')
print('Your code should only be one line long. So, instead of assigning the list to a variable, simply print the list.')

# 1. [1, 3, 7, 9, 11, 13, 15]

int_list = [ i for i in range(16) if i%2 or i%1]
print(int_list)

# 2. [1, 10, 100, 1000, 10000, 100000]

int_list = [i*10*10 for i in range(6) if i%10]
print(int_list)

#3. ["a", "aa", "aaa", "aaaa", "aaaaa", "aaaaaa"]


string_list = [i*'a' for i in range(7) if i%6]
print(string_list)

#4. [1, 9, 25, 49, 81, 121]
int_list = [ i**2 for i in range(12) if i%2 or i == 1]
print(int_list)

#5. [0, 4, 8, 12, 16, 20, 24, 28, 32, 36]

int_list = [i*4 for i in range(10) if i%1 == 0]
print(int_list)

# 6 (extra). ["l", "p", "h", "b", "t"]

i = "Alphabet"

string_list = [i for i in range (0) if i == "A" or "E" or "I" or "O" or "U" or "a" or "e" or "i" or "o" or "u"]


######### Tuples and Set ##################

print('Set data type')
nset = {2, 3, 'a',1 ,'b'}
print(nset)

print('Add method')
nset = {2, 3, 'a',1 ,'b'}
nset.add(5)
print(nset)

print('Pop method')

nset = {2, 3, "a", 1, "b"}
print(nset)
nset.pop()
print(nset)
nset.pop()
print(nset)
nset.pop()
print(nset)
nset.pop()
print(nset)
nset.pop()
print(nset)

##################### Set Theory and Methods ##########################


print('Intersection Method')

set1 = {1, 2, 5, "a", "b"}
set2 = {1, 3, 4, "a", "c"}

# order is not important
print(set1.intersection(set2))
print(set2.intersection(set1))



print('Union Method')

set1 = {1, 2, 5, "a", "b"}
set2 = {1, 3, 4, "a", "c"}

# order is not important
print(set1.union(set2))
print(set2.union(set1))

print('Union Method with the  | ')
print('which companies are likely to perform with good revenues')
corp = {'General Electric','Microsoft','Amazon'}
companies1 ={'General Electric','Proctor & Gamble','General Dynamics'}
companies2 ={'Microsoft','Berkshire Hathaway','General Dynamics'}

available_options = corp | companies1 | companies2
available_options2 = corp.union(companies1, companies2)

print(available_options)
print(available_options2)


print('Difference method')

available_options = {"pominos", "pizza no. 1", "pineapples don't belong", "pizza fusion", "father johns", "fresh slice"}
you = {"pizza no. 1"}
friend1 = {"father johns", "pominos"}
friend2 = set()     # friend 2 isn’t picky, so they don't care
remaining_options = available_options.difference(you, friend1, friend2)
remaining_options2 = available_options - you - friend1 - friend2

print(remaining_options)
print(remaining_options2)


print("isdisjoint method")

# set1 and set2 have 1, "a" in common
set1 = {1, 2, 5, "a", "b"}
set2 = {1, 3, 4, "a", "c"}
# set3 and set4 have nothing in common
set3 = {1, 2, "a", "b"}
set4 = {3, 4, "c", "d"}

print(set1.isdisjoint(set2))
print(set3.isdisjoint(set4))


print("issubset() method ")

set1 = {1, 2, "a"}
set2 = {1, 2, 3, "a", "b"}

print("set1 is a subset of set2:", set1.issubset(set2))
print("set2 is a subset of set1:", set2.issubset(set1))

print('Pratice Exercise on Sets')

# Using your understanding of subsets and supersets, given two sets (set1 and set2),
#write a program using a for loop to determine if the two sets are disjoint. Also
#determine if set1 is a subset or superset of set2. Remember that if two sets are
#disjoint, they cannot be subsets or supersets of one another.

#sNote: If the intersection set of set1 and set2 is equal to set1 (or set2), that means
#set1 and set2 have the same values.



######################code starts here################################


tuple_of_sets = ({1, 2, 3, 4}, {2, 4}, {1, 3})

m = int(input ('# Assign m a value between 0 and 2 before running the program'))
n = int(input ('# Assign m a value between 0 and 2 before running the program'))

# Declare sets that are frozen
set1 = tuple_of_sets[m]
set2 = tuple_of_sets[n]


intersection_set = set()
set = set1 & set2
intersection_common = tuple_of_sets[0].intersection(set1,set2)

for int in set1:
    if int in set2:
        intersection_set.add(int)
        print("The is not disjoint")
    if len(intersection_set) == 0:
        print("we are disjoint")

if set1 == intersection_set or set2 == intersection_set:
    # Write the conditions for the output statements
    if len(set1) < len(set2):
        print('set1 is a subset of set2')
    elif len(set1) > len(set2):
        print('Set1 is a superset of set2')
    else:
        print('Set1 is both a subset and superset of set2')

