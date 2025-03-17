if __name__ == '__main__':
    N = int(input("How many commands are you going to enter? "))
    
    # define an empty list
    my_list = list()
    
    for _ in range(N):
            command = input().split()
            cmd = command[0]
            # write down the if-else chain to check the input
            if cmd == 'insert':
                i, e = int(command[1]), int(command[2])
                my_list.insert(i, e)
            elif cmd == 'print':
                print(my_list)
            elif cmd == 'remove':
                e = int(command[1])
                my_list.remove(e)
            elif cmd == 'append':
                e = int(command[1])
                my_list.append(e)
            elif cmd == 'sort':
                my_list.sort()
            elif cmd == 'pop':
                my_list.pop()
            elif cmd == 'reverse':
                my_list.reverse()

    # print the above list after running the commands on it 
    print(my_list)
