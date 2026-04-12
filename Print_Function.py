#import print

print('Welcome to python programming !')
print("This is fun !")

#Here is how to print list, tuple, and string together using the default separator
#print(*objects, sep=' ', end='\n', file=None, flush=False)
lst = [1, 2, 3]
t = ("A", "B")
s = "Python"
print(lst, t, s)

#Here is how to print multiple objects but uses a custom separator to control spacing
lst = [1, 2, 3]
t = ("A", "B")
s = "Python"
print(lst, t, s, sep=" | ")

