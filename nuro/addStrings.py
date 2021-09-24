class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        num1, num2 = list(num1), list(num2)
        carry, res = 0, []
        
        while len(num2) or len(num1):
            n1 = ord(num1.pop()) - ord('0') if len(num1) else 0
            n2 = ord(num2.pop()) - ord('0') if len(num2) else 0
            
            tmp = n1 + n2 + carry
            res.append(tmp % 10)
            carry = tmp // 10
            
        if carry: res.append(carry)
        return ''.join([str(i) for i in res])[::-1]
    
    def addStringsV2(self, num1, num2):
        # both positive --> add two strings
        # both negative --> - (add two strings)
        # one positive, one negative --> subtract
        if num1[0] != '-' and num2[0] != '-':
            return self.addStrings(num1, num2)
        elif num1[0] == num2[0] == '-':
            return '-' + self.addStrings(num1[1:], num2[1:])
        else:
            num1_is_neg = False
            if num1[0] == '-':
                num1_is_neg = True
                num1 = num1[1:]
                c = self.compare(num1, num2)
            else:
                num2 = num2[1:]
                c = self.compare(num1, num2)
            if c == 0:
                return '0'
            elif c > 0 and not num1_is_neg:
                return self.subtractString(num1, num2)
            elif c > 0 and num1_is_neg:
                return '-' + self.subtractString(num1, num2)
            elif c < 0 and num1_is_neg:
                return self.subtractString(num2, num1)
            else:
                return '-' + self.subtractString(num2, num1)
            
    
    def compare(self, num1, num2):
        if num1 == num2: return 0
        if len(num1) > len(num2): return 1
        if len(num1) < len(num2): return -1
        for i in range(len(num1)):
            if num1[i] == num2[i]:
                continue
            else:
                return 1 if num1[i] > num2[i] else -1
        return 0


    """
    允许负数input分情况讨论：
    1. n1 n2 both positive
    2. n1 n2 both negative (remove the sign, then add 2 nums, same as case 1, add '-')
    3. one positive, one negative
        compare two nums: (除符号位以外，比较长度，长度一样时比第一位)
    1) num1 == num2: return 0
    2) num1 > num2: subtractString(num1, num2)
    3) num1 < num2: '-' + subtractString(num2, num1)
    """

    def subtractString(self, num1, num2):
        # num1 > num2
        num1, num2 = list(num1), list(num2)
        carry, res = 0, []
        
        while len(num2) or len(num1):
            n1 = ord(num1.pop()) - ord('0') if len(num1) else 0
            n2 = ord(num2.pop()) - ord('0') if len(num2) else 0

            tmp = n1 - n2 - carry
            if tmp < 0:
                carry = 1
                tmp += 10
            else:
                carry = 0
            res.append(tmp)
        ans = ''.join([str(i) for i in res])[::-1]
        # remove the first zeros
        if ans.startswith('0'):
            i = 0
            while i < len(ans):
                if ans[i] != 0:
                    break
            ans = ans[i+1:]
        return ans

sol = Solution()
print(sol.addStringsV2('12', '-13'))
