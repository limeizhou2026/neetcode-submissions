class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        count = [0] * numCourses
        q = deque()
        taken = 0
        adj = [[] for _ in range(numCourses)]
        #count how many prerequiste each course has
        for course, prerequisite in prerequisites:
            #increment by 1 if there is 
            count[course] +=1
            adj[prerequisite].append(course)

        #scan through the prerequisite number of each course, if the num is still 0 means it's ready to be taken
        for course in range(numCourses):
            if count[course] == 0:
                q.append(course)
        
        #this process would continue as long as there is course still in the queue
        while q:
            #set a variable to receive the course that has been taken
            current = q.popleft()
            #count the total course num that have been taken
            taken+=1
            #scan through the p to see which prerequisite matches with the current(prerequisite has been taken); find it and decrease teh corresponding prerequisite number of the course by 1 
            for course in adj[current]:
                #key:这里的逻辑是依赖这门课的课程都在后面的list，现在这门课已经上完了。那么相对应的这些课的prerequisite count就得减少1门
                    count[course] -=1
                    #confirm if any course is ready to be took
                    if count[course] == 0:
                        q.append(course)

        return numCourses == taken














































        #A list include 4 integers: count = [0,0,0,0]
        count = [0] * numCourses
        q = deque()
        taken = 0
        #A list include 4 list: adj  = [[],[],[],[]]
        adj = [[] for _ in range(numCourses)]
        for course, prerequisite in prerequisites:
            count[course] += 1
            #append the courses which depends on the prereuisite 
            adj[prerequisite].append(course)
            #should count all the course and prerequisite relationship and do the check if any count[course] == 0
        for course in range(numCourses):
            if count[course] == 0:
                q.append(course)
                

        while q:
            current = q.popleft()
            taken +=1
            #course in the list of course that rely on the current/prerequisite
            for course in adj[current]:
                    count[course] -= 1
                    if count[course] == 0:
                        q.append(course)


        return numCourses == taken



































        count = [0] * numCourses
        taken = set()
        q = deque()
        adj = [[] for i in range(numCourses)]
        for course, prerequisite in prerequisites:
            count[course] += 1
            adj[prerequisite].append(course)

        for course in range(numCourses):
            if count[course] == 0:
                q.append(course)
        
        while q:
            current = q.popleft()
            taken.add(current)
            for course in adj[current]:
                    count[course] -= 1
                    if count[course] == 0:
                        q.append(course)
        
        n = len(taken)

        return numCourses == n
