
# coding: utf-8

# In[1]:

def maxProductFinder(l1):
    num1 = max(l1)
    l1.remove(num1)
    l1
    num2 = max(l1)
    l1.remove(num2)
    l1
    num3 = max(l1)
    l1.remove(num3)
    l1
    l2 = []
    for x in l1:
        if x<0:
            l2.append(x)
        print l2
    num4 = min(l2)
    l2.remove(num4)
    l2
    num5 = min(l2)
    l2.remove(num5)
    l2
    l3 = [num1, num2, num3, abs(num4), abs(num5)]
    num6 = max(l3)
    l3.remove(num6)
    l3
    num7 = max(l3)
    l3.remove(num7)
    l3
    num8 = max(l3)
    result = num6*num7*num8
    print result
array = [1,2,3,4,5,6,9,10,-10,-11,12, 14, 18,20]
maxProductFinder(array)


# In[ ]:



