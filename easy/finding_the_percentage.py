# if __name__ == '__main__':
#     n = int(input())
#     avg = 0
#     total = 0
#     student_marks = {}
#     for _ in range(n):
#         name, *line = input().split()
#         scores = list(map(float, line))
#         student_marks[name] = scores
#     query_name = input()
#     score = student_marks[query_name]
#     for i in score:
#         total += i
#     avg = total/len(score)
#     print(f"{avg:.2f}")
import statistics
if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    score = student_marks[query_name]
    avg = statistics.mean(score)
    print(f"{avg:.2f}")