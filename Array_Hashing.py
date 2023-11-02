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
      hset = set()   # make a hash set to compare
      for num in nums: 
        if num in hset: # is this num in the hset?
          return True # yes, return true
        else:
          hset.add(num) # no, add it to the hset and repeat this
          
# Valid Anagram solution 1 using hashSet
class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t) : # the lengths are different. fail
            return False

        countS, countT = {}, {} # make two hash sets to compare
        for i in range(len(s)): # len(s) or len(t) doesn't matter at this point
            countS[s[i]] = 1 + countS.get(s[i],0) # countS[s[i]] starts at 0, and increases as we loop over s[i] 
                                                # get(s[i],0) is looking for s[i] char, if no exist, return 0. if exists, return the current count of s[i]
                                                # 1 + is to increment the count of s[i]
            countT[t[i]] = 1 + countT.get(t[i],0)
        for c in countS:
            if countS[c] != countT.get(c,0):  # compare the counts of the char in each set
                return False
        return True

  


# solution 2 using sort
class Solution:
  def isAnagram(self, s: str, t: str) -> bool:
    return sorted(s) == sorted(t)
      
    
