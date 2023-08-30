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




def quiz(i):
    if i > 1:
        quiz(i/2)
        quiz(i/2)
    print("*")

def test(n):
    print(f"{n}")
    if n > 0:
        test(n-2)


def test1(n):
    if n > 0:
        test1(n-2)
        print(f"({n})")

test1(4)