import random
# convert random function to uniform
def uniforml(a, b):
    x = random.random()*b
    y = random.random()*a
    print (x+y)
uniforml(-1,5)