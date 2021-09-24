"""
找到两个json file的不同并且输出，例子：
Input是两个json:  
expected = {
  id: 12,
  first_name: James,
  last_name: Paul,
  location: {
    state: CA,
    city: LA
  }
}

actual = {
  id: 20,
  first_name: James,
  location: {
    state: CA,
    city: SF
  }
}

output：
[
  [ '-', 'id',                  12              ],
  [ '-', 'last_name',           'Paul'         ],
  [ '-', 'location.city',   'LA' ],
  [ '+', 'id',                  20                ],
  [ '+', 'location.city',     'SF']               ]
]

"""


class Solution:
    def jsonDiff(self, expected: dict, actual: dict):
        old_list = []
        new_list = []
        for k, v in expected.items():
            if isinstance(v, dict):
                self.getItems([k], v, actual.get(k, {}), old_list, new_list)
            else:
                if k in actual:
                    new_v = actual[k]
                    if new_v != v:
                        old_list.append(['-', k, v])
                        new_list.append(['+', k, v])
                else:
                    old_list.append(['-', k, v])
            
        return old_list + new_list


    def getItems(self, keys, old_v, new_v, old_list, new_list):
        for k, v in old_v.items():
            if isinstance(v, dict):
                self.getItems(keys + [k], new_v.get(k, {}), old_list, new_list)
            else:
                if k in new_v and v != new_v[k]:
                    keys += [k]
                    old_list.append(['-', '.'.join(keys), v])
                    new_list.append(['+', '.'.join(keys), new_v[k]])
                elif k not in new_v:
                    keys += [k]
                    old_list.append(['-', '.'.join(keys), v])

expected = {'id': 12, 'first_name': 'James', 'last_name': 'Paul', 'location': { 'state': 'CA', 'city': 'LA'}}
actual = {'id': 20, 'first_name': 'James', 'location': { 'state': 'CA', 'city': 'SF'}}

sol = Solution()
res = sol.jsonDiff(expected, actual)    
print(res)
        