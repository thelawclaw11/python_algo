from collections import deque

class Solution:
    def countStudents(self, students, sandwiches):
        student_queue = deque(students)
        sandwiches_stack = deque(sandwiches)

        iterations_without_match = 0

        while len(student_queue) > 0 and iterations_without_match < len(student_queue):
            if student_queue[0] == sandwiches_stack[0]:
                sandwiches_stack.popleft()
                student_queue.popleft()
                iterations_without_match = 0
            else:
                student_queue.append(student_queue.popleft())
                iterations_without_match += 1

        return len(student_queue)


solution = Solution()

# 0
print(solution.countStudents([1,1,0,0],[0,1,0,1]))

# 3
print(solution.countStudents([1,1,1,0,0,1], [1,0,0,0,1,1]))