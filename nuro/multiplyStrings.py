class Solution:
    def multiplyStrings(self, num1, num2):
        if num1 == '0' or num2 == '0':
            return '0'
        res = 0
        for i, n2 in enumerate(num2[::-1]):
            pre, curr = 0, 0
            for j, n1 in enumerate(num1[::-1]):
                multi = (ord(n1) - ord('0')) * (ord(n2) - ord('0'))
                div, mod = multi // 10, multi % 10
                curr += (mod + pre) * (10 ** j)
                pre = div
            curr += pre * (10 ** len(num1))
            res += curr * (10 ** i)
        return str(res)


