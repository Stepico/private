from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs):
        d = defaultdict(list)

        for word in strs:
            key = ''.join(sorted(word))
            d[key].append(word)

        return d.values()


if __name__ == '__main__':
    s = Solution()
    print(s.groupAnagrams(["eat","tea","tan","ate","nat","bat"]))
    print(s.groupAnagrams(["",""]))

    my_tuple = [('A', 5), ('B', 7), ('A', 4), ('C', 1), ('A', 8), ('B', 3)]
    my_dict = defaultdict(list)

    for k, v in my_tuple:
        my_dict[k].append(v)

    a = {k: sum(my_dict[k]) for k in my_dict}
    # OR
    b = {k: sum(v) for k, v in my_dict.items()}
    print(a, b)