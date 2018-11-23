def tic_tac_toe() :
    board=[1,2,3,4,5,6,7,8,9]
    end=False
    win_combinations=((0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(1,4,8),(2,4,6))

    def draw() :

        print("   |   |   ")
        print(" "+str(board[0])+" |"+ str(board[1])+"  | "+str(board[2])+" ")
        print("---|---|---")
        print("   |   |   ")
        print(" "+str(board[3])+" |"+str(board[4])+"  | "+str(board[5])+" ")
        print("---|---|---")
        print("   |   |   ")
        print(" "+str(board[6])+" |"+str(board[7])+"  | "+str(board[8])+" ")
        print("---|---|---")
        print("   |   |   ")

    def p1() :
        n=choose_number()
        if board[n] == "X" or board[n] =="O" :
            print("\nYOU CAN'T GO THERE . TRY AGAIN !!!")
            p1()
        else :
            board[n]="X"

    def p2() :
        n=choose_number()
        if board[n] == "X" or board[n] =="O" :
            print("\nYOU CAN'T GO THERE . TRY AGAIN !!!")
            p2()
        else :
            board[n]="O"
    def choose_number() :
        while True :
            a=input()
            try :
                a=int(a)
                a-=1
                if a in range (0,9) :
                    return a
                else :
                    print("\nTHAT'S NOT ON THE BOARD . TRY AGAIN")
                    continue
            except :
                print("\nTHAT'S NOT A NUMBER . TRY AGAIN")
                continue
    def check_board() :
        count=0
        for a in win_combinations :

            if board[a[0]] == board[a[1]] == board[a[2]] == "X" :
                print("PLAYER 1 WINS!!\n")
                print("CONGRATULATIONS!!\n")
                return True

            if board[a[0]] == board[a[1]] == board[a[2]] == "O" :
                print("PLAYER 1 WINS!!\n")
                print("CONGRATULATIONS!!\n")
                return True
        for a in range(9) :
            if board[a]== "X" or board[a]=="O" :
                count+=1
            if count==9 :
                print("THE GAME ENDS HERE IN A TIE!!\n")
                return True

    while not end :
        draw()
        end=check_board()
        if end== True :
            break
        print("PLAYER 1 CHOOSE WHERE TO PLACE A CROSS")
        p1()
        print()
        draw()
        end=check_board()
        if end== True :
            break
        print("PLAYER 2 CHOOSE WHERE TO PLACE A NOT ")
        p2()
        print()

    if input("PLAY AGAIN (y/n)")=="y" :
        print()
        tic_tac_toe()
tic_tac_toe()
