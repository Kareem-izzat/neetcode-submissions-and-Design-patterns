"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        
        if not node:
            return None

        clones = {}

        # Initialize BFS
        q = deque([node])
        clones[node] = Node(node.val)

        # BFS traversal
        while q:
            curr = q.popleft()

            for nei in curr.neighbors:
            
                if nei not in clones:
                    clones[nei] = Node(nei.val)
                    q.append(nei)

                # Link clone of current to clone of neighbor
                clones[curr].neighbors.append(clones[nei])

        return clones[node]
            