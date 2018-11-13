class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s is None or len(s) == 0:
            return 0
        if len(s) == 1:
            return 1
        if len(s) == 2:
        	if s[0] == s[1]:
        		return 1
        	else:
        		return 2
        #全局变量，存储最长不重复长度
        max_len = 0
        for i in range(len(s)):
            #使用字典存储
            str_dict = {}
            str_len = 0
            for j in range(i,len(s)):
                if s[j] in str_dict:
                    break
                else:
                    str_dict[s[j]] = j
                    str_len = str_len + 1
            if str_len >= max_len:
                max_len = str_len
        return max_len

#2018.11.06

#-------------------官方主函数------------------------

def stringToString(input):
    return input[1:-1].decode('string_escape')

def main():
    import sys
    import io
    def readlines():
        for line in io.TextIOWrapper(sys.stdin.buffer, encoding='utf-8'):
            yield line.strip('\n')

    lines = readlines()
    while True:
        try:
            line = next(lines)
            s = stringToString(line);
            
            ret = Solution().lengthOfLongestSubstring(s)

            out = str(ret);
            print(out)
        except StopIteration:
            break

if __name__ == '__main__':
    main()