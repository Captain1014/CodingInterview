# Questions
# Contains Duplicate
# Valid Anagram




# Answers
# Contains Duplicate
class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
      hset = set()
      for num in nums:
        if num in hset:
          return True
        else:
          hset.add(num)
          
# Valid Anagram solution 1 using hashSet
class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t) :
            return False

        countS, countT = {}, {}
        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i],0)
            countT[t[i]] = 1 + countT.get(t[i],0)
        for c in countS:
            if countS[c] != countT.get(c,0):
                return False
        return True

  
  # why do we use get?

# solution 2 using sort
class Solution:
  def isAnagram(self, s: str, t: str) -> bool:
    return sorted(s) == sorted(t)
      
    
