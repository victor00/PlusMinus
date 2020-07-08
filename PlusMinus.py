import math
import os
import random
import re
import sys


def plusMinus(arr):
    #n is the size of array // number of elements of the array
    count_positive = len(list(filter(lambda x:(x>0), arr)))
    count_zero = len(list(filter(lambda x:(x==0), arr)))
    count_negative = len(list(filter(lambda x:(x<0), arr)))

    result = [count_positive, count_negative, count_zero]

    for x in result:
        print("{:10.4f}".format(float(x/n)))
