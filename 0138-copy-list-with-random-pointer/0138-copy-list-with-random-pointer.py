"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        
        if not head:
            return None
        
        # Dictionary: original node -> copied node
        old_to_new = {}
        
        # Pass 1: Create all copied nodes
        current = head
        
        while current:
            old_to_new[current] = Node(current.val)
            current = current.next
        
        
        # Pass 2: Connect next and random pointers
        current = head
        
        while current:
            
            copy_node = old_to_new[current]
            
            # Connect next
            if current.next:
                copy_node.next = old_to_new[current.next]
            
            # Connect random
            if current.random:
                copy_node.random = old_to_new[current.random]
            
            current = current.next
        
        
        return old_to_new[head]


  