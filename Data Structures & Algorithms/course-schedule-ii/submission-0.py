class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        #initialize a count list to count the prerequisite for each course
        count=[0]*numCourses #since we modify the value for each index so change create an empty array
        #initialize a result list without size since we append the value
        result = []
        q=deque()
        finished = 0
        adj_list = [[] for i in range(numCourses)]
        #scan thorugh the whole course pairs to see the number of prerequisites for each course, course number as the index 
        for course, prerequisite in prerequisites:
            count[course] += 1
            #append the corresponding course to the prerequisite, prerequisite value as the outer inder
            adj_list[prerequisite].append(course)

        #go through the count number of each course, if the count is 0 which means it's ready to take
        for course in range(numCourses):
            if count[course] == 0:
                #append course to the queue
                q.append(course)

        while q:
            #pop up the course that was finished
            current = q.popleft()
            #it should be added to teh result
            result.append(current)
            #incremente the finished number by 1
            finished+=1
            #using current as index, current here is a "prereuisite". Any course has it as prerequisite, the count can be decreased by 1
            for course in adj_list[current]:
                count[course] -= 1
                #check again if any count equal to 0/ready to take:
                if count[course] == 0:
                    q.append(course)

        #finally check if finished course number equal to numCourses, return final result as needed
        if finished == numCourses:
            return result
        else:
            return []