﻿"""Given a 32-bit signed integer, reverse digits of an integer.

Example 1:

Input: 123
Output:  321
Example 2:

Input: -123
Output: -321
Example 3:

Input: 120
Output: 21
Note:
Assume we are dealing with an environment which could only hold integers within the 32-bit signed integer range. For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.
"""

import operator as op
"""
lt(a,b)相当于 a<b     从第一个数字或字母（ASCII）比大小 
le(a,b)相当于a<=b
eq(a,b)相当于a==b     字母完全一样，返回True,
ne(a,b)相当于a!=b
gt(a,b)相当于a>b
ge(a,b)相当于 a>=b
"""
import math
"""abs() 是内置函数。 fabs() 函数在 math 模块中定义\
fabs() 函数只对浮点型跟整型数值有效。 abs() 还可以运用在复数中"""
class Solution:    
    def reverse(self, x):
        s = op.ge(x, 0)
        if s == 0:
            x = -x
            s = -1
        lst = []    
        r = 0
        while x:
            lst.append(x%10)
            x=x//10
            r = r*10 + lst.pop()                    
        return s*r * (math.fabs(r) < 2**31)
