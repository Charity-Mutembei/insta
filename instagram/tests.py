from django.test import TestCase

# Create your tests here.
def get_middle(s):
    x = len(s)
    y = int(x/2)
    if x%2 == 0:
        print (s[y-1:y+1])
    else:
        print( s[y:y+1])
get_middle('boy')