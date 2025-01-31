import colorama




values = [(0, 2), (1, 1), (2, 1), (3, 0), (4, 0), (5, 0)]
example = [[3, 1, 7, 4, 2], [2, 3, 1, 1, 1], [1, 2, 1, 1, 8], [2, 1, 1, 5, 3], [2, 1, 4, 4, 4], [5, 2, 7, 5, 1]]


def PrettyCamino(M,C):
    l,c = len(M),len(M[0])
    padding = 2
    left_pipe = 1
    final_pipe = 1
    n = 0
    width = c  * (n + padding + final_pipe +1) +1

    for _ in range(width):
            print("-",end="")
    print() 
    for i in range(l):
        print("|",end="")
        for j in range(c):

                if((i,j) in C):
                    print(colorama.Fore.RED + " " +str(M[i][j]) + colorama.Fore.WHITE + " |",end="")
                else:
                    print(colorama.Fore.WHITE +" " +str(M[i][j]) + " |", end="")
        print()    
        for _ in range(width):
            print("-",end="")
        print()
    print("\n")

    print("Values : [ ",end="")
    sum_ = 0
    for i in range(0,len(C)-1):
         print(f"{M[C[i][0]][C[i][1]]},",end="")
         sum_ += M[C[i][0]][C[i][1]]
    print(f"{M[C[-1][0]][C[-1][1]]} ",end="")
    sum_ += M[C[-1][0]][C[-1][1]]
    print("]", end="")
    print(f"    Total = {sum_}")

PrettyCamino(example,values)
