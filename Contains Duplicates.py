array = []
n = int(input("How many elements you got fella? "))
print("Alright! Put " + str(n) + " elements:" )
for i in range(0, n):
  element = int(input())
  array.append(element)


print("Checking if they have dupliactes(True if they do): " )

def containsDuplicate(nums):
  hashset = set()
  for n in nums:
    if n in hashset:
      return True
    hashset.add(n)
  return False

print(containsDuplicate(array))