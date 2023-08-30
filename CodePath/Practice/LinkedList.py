# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

'''
Understand
Input: head of linked list
Output: head of edited linked list
1. Removing nth node from the end of list
2. Does not have to be sorted
3. Singly Linked list

Match
Temporary head 


'''





class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = self.right = None

    def sum_of_left_leaves(root):
        def helper(root, counter):
            while root:
                if root.left == None:
                    root.val += counter
                else:
                    helper(root.left, counter) and helper(root.right, counter)
        sumLeft = 0
        helper(root, sumLeft)
        return (sumLeft)
    


teamA = [1, 4, 6]
teamB = [2, 3, 5]

for num in teamB:
    teamA.append(num)
    teamA.sort()

list1 = [1, 2]
list2 = [3, 4]
list1.extend(list2)
print(list1)