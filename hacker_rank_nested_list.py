if __name__ == '__main__':

     # create a list for grades
    grades = list()

    # create a list for names
    names = list()

    for _ in range(int(input())):
        name = input()
        score = float(input())

        # keep appending the new names
        names.append(name)

        # keep appending the new grades
        grades.append(score)

    # define a new list that contains lists (which will contains name, grade)
    names_grades = list()

    # put the name and corresponding grade in a list and append it to a new list
    for name, grade in zip(names, grades):
        names_grades.append([name, grade])

    # sort the grades in ascending order
    sorted_grades = sorted(grades)

    # find the second lowest grades(s)
    second_lowest_grade_s = list()

    # find out the unique grades
    unique_grades = set(grades)

    # print the set
    # print(unique_grades)

    # make an ordered list 
    ordered_list_grades = sorted(list(unique_grades))

    # print the ordered list
    # print(ordered_list_grades)

    # create another list that will contain the sorted names
    lowest_scorers = list()

    # check the records and match the second lowest grade with their grades
    for rec in names_grades:
        if rec[1] == ordered_list_grades[1]:
            lowest_scorers.append(rec[0])


    # sort the lowest scorers names
    lowest_scorers_sorted = sorted(lowest_scorers)

    for name in lowest_scorers_sorted:
        print(name)
