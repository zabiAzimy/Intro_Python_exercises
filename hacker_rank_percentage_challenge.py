if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores

    # we have a dictionary with keys as names 
    # the value of that dictionary will be list of scores

    # take a query name from user
    query_name = input()

    # Percentage of the given student
    percentage = sum(student_marks[query_name]) / len(student_marks[query_name]) 
    print(f"{percentage:.2f}")

