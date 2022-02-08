# 290. 单词规律
# 给定一种规律 pattern 和一个字符串 str ，判断 str 是否遵循相同的规律。
# 这里的 遵循 指完全匹配，例如， pattern 里的每个字母和字符串 str 中的每个非空单词之间存在着双向连接的对应规律。
# 示例1:

# 输入: pattern = "abba", str = "dog cat cat dog"
# 输出: true

# 示例 2:

# 输入:pattern = "abba", str = "dog cat cat fish"
# 输出: false

# 示例 3:

# 输入: pattern = "aaaa", str = "dog cat cat dog"
# 输出: false

# 示例 4:
# 输入: pattern = "abba", str = "dog dog dog dog"
# 输出: false

# 说明:
# 你可以假设 pattern 只包含小写字母， str 包含了由单个空格分隔的小写字母。
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        slist = s.split(" ")
        if len(pattern) != len(slist):
            return False
        else:
            mydict = {}
            for i in range(len(pattern)):
                if pattern[i] not in mydict and slist[i] not in mydict.values():
                    mydict[pattern[i]] = slist[i]
                else:
                    if pattern[i] in mydict:
                        if mydict[pattern[i]] != slist[i]:
                            return False
            if len(mydict) != len(set(pattern)):
                return False
            else:
                return True


a = Solution()
print(a.wordPattern("abba", "dog dog dog dog"))
# def wordPattern(self, pattern: str, str: str) -> bool:
#     res=str.split()
#     return list(map(pattern.index, pattern))==list(map(res.index,res))
