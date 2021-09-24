class Solution:
    def __init__(self, s):
        self.dic = {}
        self.process(s)
    

    def process(self, s):
        s = s.split('\n')
        for substr in s:
            level, substr = self.cnt_space(substr)
            substr = substr.split(':')
            key = substr[0]
            val = substr[1] if substr[1] != '' else {}
            if level > 0:
                new_key = list(self.dic.keys())[-1]
                self.update(self.dic, new_key, key, val, level)
            else:
                self.dic[key] = val


    def update(self, tmp_dict, tmp_key, my_key, my_val, level):
        if(isinstance(tmp_dict[tmp_key], dict)) and level > 0:
            level -= 2
            if tmp_dict[tmp_key] == {}:
                tmp_dict[tmp_key][my_key] = my_val
                return
            self.update(tmp_dict[tmp_key], list(tmp_dict[tmp_key].keys())[-1], my_key, my_val, level)
        else:
            tmp_dict[my_key] = my_val
    

    def cnt_space(self, s):
        i = 0
        cnt = 0
        while i < len(s):
            if s[i] == ' ':
                cnt += 1
                i += 1
            else:
                break
        return cnt, s[cnt:]
    

    def get_val(self, keys):
        tmp = self.dic
        for k in keys:
            if k not in tmp:
                raise Exception('Key does not exist')
            else:
                tmp = tmp[k]  
        return tmp


txt_input = "K1:V1\nK2:V2\nK3:\n  K31:V31\n  K32:\n    K321:V321\n    K322:V322\n  K33:V33\nK4:\n  K41:V41\n  K42:V42"
sol = Solution(txt_input)
print(sol.get_val(['K3', 'K31']))



