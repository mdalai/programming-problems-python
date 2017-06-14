class Solution:
    def addBoldTag(self, s, dict):
        """
        :type s: str
        :type dict: List[str]
        :rtype: str
        """
        index_list = []
        begin_index = -1
        end_index = -1
        for p in dict:
            if s.find(p) != -1:
                begin_index = s.find(p)
                if begin_index <= end_index: # overlap and consecutive
                    end_index = begin_index + len(p)
                    index_list[-1][1] = end_index
                    continue
                end_index = begin_index + len(p) 
                index_list.append([begin_index, end_index])
                
        print(index_list)

        s2 = ""
        start_idx = 0
        for idx in index_list:
            s2 = s2 + s[start_idx:idx[0]] + '<b>' + s[idx[0]:idx[1]] + '</b>'
            start_idx = idx[1]
        #print(s2)
        s2 = s2 + s[start_idx:]

        return s2


            
s = "abcxyz123"
dict = ["abc","123"]
'''s = "aaabbcc"
dict = ["aaa","aab","bc"]   '''         
solution = Solution()
s2 = solution.addBoldTag(s,dict)
print(s2)