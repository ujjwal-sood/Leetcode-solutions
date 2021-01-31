"""
# DFS
class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return node
        d, visit = {node: Node(node.val)}, {}
        
        def dfs(node):
            if node in visit:
                return 
            visit[node] = -1
            
            for neighbor in node.neighbors:
                if neighbor not in d:
                    d[neighbor] = Node(neighbor.val)
                d[node].neighbors.append(d[neighbor])
                dfs(neighbor)     
        dfs(node)
        return d[node]
"""
		
# BFS
class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return node
        d = {node: Node(node.val)}
        q = collections.deque([(node)])
        
        while q:
            cur = q.popleft()
                
            for neighbor in cur.neighbors:
                if neighbor not in d:
                    d[neighbor] = Node(neighbor.val)
                    q.append(neighbor)
                d[cur].neighbors.append(d[neighbor])
        return d[node]