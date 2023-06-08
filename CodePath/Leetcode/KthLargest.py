class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        pass

    def add(self, val: int) -> int:
        pass
"""
U
* goal: define __init__ and add() member functions
* add: append input to object and return Kth largest element
    ** access to k, nums
* Code under Explanation is what the programmer will execute after we define this class
* input type:
    * integers only?
    * nums has to be at least k items long
M
* if input is sorted (desc), finding the kth largest element is easy and O(1), just return nums[k-1]
* maxHeap:
    * have some order to them
    * maxHeap.pop() will return largest element
    
P
INTIALIZE OBJECT:
* keep only the top k elements in stream 
    heapify input --> minHeap
    until size is k,
        pop from minheap
ADD DATA TO OBJECT:
    insert element into minHeap
    pop from minHeap
    return(minHeap[0])
I
R
E
"""

# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)