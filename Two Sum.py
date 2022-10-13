#Given an array of integars, return indices of two numbers such that they add up to a specific target. Assume there will be exactly one solution.

nums = [2, 7, 11, 15] #target = 9, so return [0,1]
target = 9

def twoSum(numbers):
  prevMap = {}  #val : index
  for i, n in enumerate(numbers):
    diff = target - n
    if diff in prevMap:
      return [prevMap[diff], i]
    prevMap[n] = i
  return

print(twoSum(nums))

