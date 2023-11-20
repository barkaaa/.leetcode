#
# @lc app=leetcode.cn id=93 lang=python
#
# [93] 复原 IP 地址
#

# @lc code=start
class Solution(object):
    
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        
        resList = []
        def findIpList(s,numList):
            if len (numList) < 4:
                if len(s) == 0:
                    return None
            elif len(numList)>4:
                return None
            elif len(numList) == 4:
                if len(s) == 0:
                    return numList
                else:
                    return None
            
            num = ""
            r = len(s) if len(s)<=3 else 3
            for i in range(r):
                
                num += s[i]
                if len(num) > 1 and int(num) <= 255 and not num.startswith('0') or int(num) < 10 and len(num) == 1:
                    numList.append(num)
                    res = findIpList(s[i+1:],numList)
                    if res != None:
                        resList.append('.'.join(numList))
                        numList.pop(len(numList) - 1)
                    else:
                        numList.pop(len(numList) - 1)
        findIpList(s,[])                
        return resList    
        

sol = Solution()
print(sol.restoreIpAddresses("25525511135"))


# @lc code=end

