class Solution:
    def runningSum(self, nums):
      numsum = 0
      answers = []
      for i in nums:
        numsum += i
        answers.append(numsum)
      return answers
