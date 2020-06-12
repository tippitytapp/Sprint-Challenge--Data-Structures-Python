'''***!Important!*** If you are running this using PowerShell by clicking on the green play button, you will get an error that `names1.txt` is not found.  To resolve this, run it, get the error, then `cd` into the `names` directory in the `python` terminal that opens in VSCode.

Navigate into the `names` directory. Here you will find two text files containing 10,000 names each, along with a program `names.py` that compares the two files and prints out duplicate name entries. Try running the code with `python3 names.py`. Be patient because it might take a while: approximately six seconds on my laptop. What is the runtime complexity of this code?'''
initial_runtime_complexity = 'O(n log (n))'
'''Six seconds is an eternity so you've been tasked with speeding up the code. Can you get the runtime to under a second? Under one hundredth of a second?

*You may not use the built in Python list, set, or dictionary in your solution for this problem.  However, you can and should use the provided `duplicates` list to return your solution.*

(Hint: You might try importing a data structure you built during the week)
'''
binary_search_tree = 'Are we suppose to use the binary search tree? thats the only one that we made that has a "contains" mentod???? and it has a much better runtime complexity of O(log (n))'
final_runtime_complexity = 'O(log (n))'
import time

# start_time = time.time()

# f = open('names_1.txt', 'r')
# names_1 = f.read().split("\n")  # List containing 10000 names
# f.close()

# f = open('names_2.txt', 'r')
# names_2 = f.read().split("\n")  # List containing 10000 names
# f.close()

# duplicates = []  # Return the list of duplicates in this data structure

# # Replace the nested for loops below with your improvements
# for name_1 in names_1:
#     for name_2 in names_2:
#         if name_1 == name_2:
#             duplicates.append(name_1)

# end_time = time.time()
from BST import BSTNode
fin_start_time = time.time()

f = open('names_1.txt', 'r')
bst_names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
bst_names_2 = f.read().split("\n")  # List containing 10000 names
f.close()
# initialize an empty list for the duplicates
bst_duplicates = []
# initialize the BSTNode
names_bst = BSTNode('findnames')
# for every name in the first list
for name in bst_names_1:
    # add every name to the binary search tree
    names_bst.insert(name)
# for every name in teh second list
for name in bst_names_2:
    # check to see if the binary search tree already contains that name
    if names_bst.contains(name):
        # if it does, add it to the duplicates list
        bst_duplicates.append(name)

fin_end_time = time.time()

print(f"{len(bst_duplicates)} duplicates: \n\n{',' .join(bst_duplicates)}\n\n")
# print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
# print (f"initial runtime: {end_time - start_time} seconds") # with the nested loops implementation it took 15.864028692245483 seconds to run. 
print(f"final tuntime: {fin_end_time - fin_start_time} secones")
print(f"\ninitial runtime complexity: {initial_runtime_complexity}, final runtime complexity: {final_runtime_complexity}\n")






# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.
