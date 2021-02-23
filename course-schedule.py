from collections import defaultdict
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
    	#Using BFS 
        G = [[] for i in range(numCourses)]
        degree = [0] * numCourses
        for j, i in prerequisites:
            G[i].append(j)
            degree[j] += 1
        bfs = [i for i in range(numCourses) if degree[i] == 0]
        for i in bfs:
            for j in G[i]:
                degree[j] -= 1
                if degree[j] == 0:
                    bfs.append(j)
        return len(bfs) == numCourses

        #Using DFS 
        """
        graph=defaultdict(list)
        l=[0]*numCourses
        
        for x in prerequisites:
            if x[0]==x[1]:
                return False
            graph[x[0]].append(x[1])
                      
        for i in range(numCourses):
            if self.topological(i,l,graph)==False:
                return False
        return True
        

    
	    def topological(self,i,l,graph):
	        if l[i]==-1:
	            return False
	        if l[i]==1:
	            return True
	        l[i]=-1
	        for x in graph[i]:
	            if not self.topological(x,l,graph):
	                return False
	        l[i]=1
	        return True
	    """