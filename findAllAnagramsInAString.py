class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """

        ls = len(s)
        lp = len(p)

        if ls < lp:
            return []

        pDict = {}
        for x in p:
            if x in pDict:
                pDict[x] += 1
            else:
                pDict[x] = 1

        result = []
        sDict = {}
        for x in s[:lp]:
            if x in sDict:
                sDict[x] += 1
            else:
                sDict[x] = 1

        if sDict == pDict:
            result.append(0)

        for i in xrange(1, ls-lp+1):
            sDict[s[i-1]] -= 1
            if sDict[s[i-1]] == 0:
                del sDict[s[i-1]]

            if s[i+lp-1] in sDict:
                sDict[s[i+lp-1]] += 1
            else:
                sDict[s[i+lp-1]] = 1

            if sDict == pDict:
                result.append(i)

        return result
    