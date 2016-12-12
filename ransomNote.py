class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """

        """
        ransomCnt = collections.Counter(ransomNote)
        magazineCnt = collections.Counter(magazine)
        return not ransomCnt - magazineCnt
        """

        magazineDic = {}
        for x in magazine:
            if x in magazineDic:
                magazineDic[x] += 1
            else:
                magazineDic[x] = 1

        for x in ransomNote:
            if x in magazineDic:
                if magazineDic[x] <= 0:
                    return False
                else:
                    magazineDic[x] -= 1
            else:
                return False

        return True


