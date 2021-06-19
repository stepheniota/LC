'''
leetcode 207 - course schedule
There are a total of numCourses courses you have to take,
labeled from 0 to numCourses - 1. You are given an array 
prerequisites where prerequisites[i] = [ai, bi] indicates 
that you must take course bi first if you want to take course ai.
Return true if you can finish all courses. Otherwise, return false.
'''
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # courses = { key=course: val=[pre_rec]}
        VISITED = 1
        STILL_VISITING = 0
        
        if not prerequisites:
            return True
        
        visited = {}
        courses = { i : [] for i in range(numCourses)}
        for c, p in prerequisites:
            courses[c].append(p)
            
        def dfs(c: int) -> bool:
            if c in visited:
                if visited[c] == STILL_VISITING:
                    return False
            
            visited[c] = STILL_VISITING
            prerecs = courses[c]
            if not prerecs:
                visited[c] = VISITED
                return True
            
            for p in prerecs:
                if p in visited:
                    if visited[p] == VISITED:
                        continue #visited[c] = VISITED
                    elif visited[p] == STILL_VISITING:
                        return False
                elif p not in courses:
                    visited[p] = VISITED
                elif not dfs(p):
                    return False
            visited[c] = VISITED
            return True
        
        for c in courses:
            if not dfs(c):
                return False
                       
        return True
                
