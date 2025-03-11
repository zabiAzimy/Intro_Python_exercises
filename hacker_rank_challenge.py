if __name__ == '__main__':
    # we take the inputs from user for the following variables
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    
    # define a list for all the permutations
    permutation_list = list()

    # write some nested loops
    for i in range(x+1):
        for j in range(y+1):
            for k in range(z+1):
                permutation_list.append([i, j, k])

    # print the permutations list
    # print(permutation_list)

    # define another list
    not_equal_to_n_list = list()

    # now take only the lists that sum of its elements in not equal to n
    for per_list in permutation_list:
        if sum(per_list) != n:
            not_equal_to_n_list.append(per_list)
    
    # print the list that do not sum to 'n'
    # print(not_equal_to_n_list)


    ## ==== Let's do all the above tasks using list comprehension
    permutation_list_1 = list()

    # using list comprehension, put all the possible permutations
    permutation_list_1 = [[i, j, k] for i in range(x+1) for j in range(y+1) for k in range(z+1)]

    # print the above list
    print(permutation_list_1)

    # check each element of the above list, remove the ones that sum up to n
    permutation_list_final = [l for l in permutation_list_1 if sum(l) != n]

    # print the final list
    print(permutation_list_final)