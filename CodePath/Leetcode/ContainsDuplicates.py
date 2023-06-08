# Testing 
#Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

#Examples
#Input: nums = [1,2,3,1]
#Output: true

#Input: nums = [1,2,3,4]
#Output: false

#Input: nums = [1,1,1,3,3,4,3,2,4,2]
#Output: true


# MATCHING
# How to use set() data structure?
# # convert input to set datastructure . check if length of set = lenght of nums then all nums elements are unique
# # if we convert input to set datastructure (which removes dupes) and its equal to original input, then unique

# Use hash tables
# create a hash table to map frequency of each number and return true if one number appears twice or more

#implementation
#since set() is more efficient (O(n)), we will implement the first proposed solution

def containsDuplicates(nums):
  if set(nums) == nums:
    return False
  else:
    return True
    
    
def containsDuplicates(nums):
	return len(set(nums)) != len(nums)
    
## REVIEW

### EMRYS SOLUTION
nums = [1,1,1,3,3,4,3,2,4,2]
# set(nums) = [1,3,4,2]
set(nums) == nums # THIS MAY BE A BUG, BUT 

### JAMIE SOLUTION
nums = [1,1,1,3,3,4,3,2,4,2]
len(set(nums)) # 4
len(nums) # 10
	# return len(set(nums)) != len(nums)
  # return True



## EVALUATE

# Time comlpexity: O(n)


# Space Complexity: 


#Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

#You may assume that each input would have exactly one solution, and you may not use the same element twice.

#You can return the answer in any order.

##UNDERSTAND
# domain of elements (negative allowed?)
# any sorting in the input array?
# 

##MATCH
# hash tables
# 

##PLAN
# go through input array and create hash table with key = nums element and value = index : O(n)
# Go through input array and, for reach element find missing = target - element 
# # Look for missing in dictionary. If found, return index : O(n)

#nums = [2,7,11,15], target = 9



'''
def twoSum():
	target = 9
  
  dict = {7:1, 2:0, 11: 2, 15: 3}
  
	for number in nums:
  	a = target - number
    if a in dict.keys():
    		return number & dict[a]
    
  	
--

frequencies = defaultdict(lambda: 0)
for ele in nums:
	frequencies[ele] = nums.index()

for (i = 0; i < len(nums); i++)

'''
