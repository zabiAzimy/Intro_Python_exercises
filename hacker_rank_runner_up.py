if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    
    # I don't know about maps in Python 
    arr_list = list(arr)

    # sort the list
    arr_list_sorted = sorted(arr_list)

    # Print the runner up score
    print(sorted(list(set(arr_list_sorted)))[-2])

