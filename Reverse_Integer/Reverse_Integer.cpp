/*Given a 32-bit signed integer, reverse digits of an integer.

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
*/

class Solution {
public:
    int reverse(int x) {
        long long ans = 0;
        while (x) {
            long long temp = ans * 10 + x % 10;
            ans = temp;
            x /= 10;
        }
        if(ans < std::numeric_limits<int>::min() || 
           ans > std::numeric_limits<int>::max())
            return 0;
        
        return ans;
    }
};