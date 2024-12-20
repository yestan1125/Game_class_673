def make_list(total_row) :
    diagram="+-----+-----+-----+-----+-----+-----+-----+"
    count1=0
    while count1<6 :
        print(diagram)
        print("| ",total_row[count1][0]," | ",total_row[count1][1]," | ",total_row[count1][2]," | ",total_row[count1][3]," | ",total_row[count1][4]," | ",total_row[count1][5]," | ",total_row[count1][6]," |")
        count1=count1+1
    print(diagram)
    print("|"," A ","|"," B ","|"," C ","|"," D ","|"," E ","|"," F ","|"," G ","|")
    print(diagram)

def Spillover_judgment (t_r,co) :
    #t_r representatives the total_row, co representatives the column 
    judge="full"
    #judge give the rusult of if the column is full
    if t_r[0][co]==" " :
        judge="not_full"
    else :
        judge="full"
    return judge

def column_judgement(col) :
    #col representatives the column 
    count_judgement=0
    #count_judgement is used for helping judge if the column is right
    judgement="wrong"
    #judgement givs the result of if the column is right
    while count_judgement<7 :
        if col==int(count_judgement ):
            judgement="right"
            break
        else :
            count_judgement+=1
    return judgement

def Judge_the_victory(total_row) :
    judgement="to_be_continued"
    winner="none"
    row=0
    column=0
    count_judge_r=0
    #count_judge_r is used for record the column
    while count_judge_r<=5 :
        count_judge_c=0
        #count_judge_c is used for record the column
        while count_judge_c<=3 :
            if total_row[row+count_judge_r][column+count_judge_c]==total_row[row+count_judge_r][column+count_judge_c+1]==total_row[row+count_judge_r][column+count_judge_c+2]==total_row[row+count_judge_r][column+count_judge_c+3]=="O" :
                print("Player 1 wins!")
                judgement="finished"
                winner="Player 1"
                break
            elif total_row[row+count_judge_r][column+count_judge_c]==total_row[row+count_judge_r][column+count_judge_c+1]==total_row[row+count_judge_r][column+count_judge_c+2]==total_row[row+count_judge_r][column+count_judge_c+3]=="X" :
                print("Player 2 wins!")
                judgement="finished"
                winner="Player 2"
                break
            else :
                count_judge_c+=1
        if judgement=="finished" :
            break
        else :
            count_judge_r+=1
    
    if judgement=="to_be_continued" :
        count_judge_c=0
        while count_judge_c<=6 :
            count_judge_r=0
            while count_judge_r<=2 :
                if total_row[row+count_judge_r][column+count_judge_c]==total_row[row+count_judge_r+1][column+count_judge_c]==total_row[row+count_judge_r+2][column+count_judge_c]==total_row[row+count_judge_r+3][column+count_judge_c]=="O" :
                    print("Player 1 wins!")
                    judgement="finished"
                    winner="Player 1"
                    break
                elif total_row[row+count_judge_r][column+count_judge_c]==total_row[row+count_judge_r+1][column+count_judge_c]==total_row[row+count_judge_r+2][column+count_judge_c]==total_row[row+count_judge_r+3][column+count_judge_c]=="X" :
                    print("Player 2 wins!")
                    judgement="finished"
                    winner="Player 2"
                    break
                else :
                    count_judge_r+=1
            if judgement=="finished" :
                break
            else :
                count_judge_c+=1

    if judgement=="to_be_continued" :     
        count_judge_r=0
        while count_judge_r <=2 :
            count_judge_c=0
            while count_judge_c<=3 :
                if total_row[row+count_judge_r][column+count_judge_c]==total_row[row+count_judge_r+1][column+count_judge_c+1]==total_row[row+count_judge_r+2][column+count_judge_c+2]==total_row[row+count_judge_r+3][column+count_judge_c+3]=="O" :
                    print("Player 1 wins!")
                    judgement="finished"
                    winner="Player 1"
                    break
                elif total_row[row+count_judge_r][column+count_judge_c]==total_row[row+count_judge_r+1][column+count_judge_c+1]==total_row[row+count_judge_r+2][column+count_judge_c+2]==total_row[row+count_judge_r+3][column+count_judge_c+3]=="X" :
                    print("Player 2 wins!")
                    judgement="finished"
                    winner="Player 2"
                    break
                else :
                    count_judge_c+=1
            if judgement=="finished" :
                break
            else :
                count_judge_r+=1
    
    if judgement=="to_be_continued" :
        count_judge_r=5
        while count_judge_r>=3 :
            count_judge_c=0
            while count_judge_c<=3 :
                if total_row[row+count_judge_r][column+count_judge_c]==total_row[row+count_judge_r-1][column+count_judge_c+1]==total_row[row+count_judge_r-2][column+count_judge_c+2]==total_row[row+count_judge_r-3][column+count_judge_c+3]=="O" :
                    print("Player 1 wins!")
                    judgement="finished"
                    winner="Player 1"
                    break
                elif total_row[row+count_judge_r][column+count_judge_c]==total_row[row+count_judge_r-1][column+count_judge_c+1]==total_row[row+count_judge_r-2][column+count_judge_c+2]==total_row[row+count_judge_r-3][column+count_judge_c+3]=="X" :
                    print("Player 2 wins!")
                    judgement="finished"
                    winner="Player 2"
                    break
                else :
                    count_judge_c+=1
            if judgement=="finished" :
                break
            else :
                count_judge_r-=1
    return judgement,winner
                   
def game():
    #total_list is designed for storing information
    row3=[" "," "," "," "," "," "," "]
    row5=[" "," "," "," "," "," "," "]
    row7=[" "," "," "," "," "," "," "]
    row9=[" "," "," "," "," "," "," "]
    row11=[" "," "," "," "," "," "," "]
    row13=[" "," "," "," "," "," "," "]
    total_row=[row3,row5,row7,row9,row11,row13]
    result="to_be_continued"
    print("Welcome to Connect 4")
    print("  1.New Two-Player Games")
    print("  2.Exit")
    choice=int(input())
    #chioce is used for starting the game
    if choice==2 :
        print("Welcome to Connect 4")
        print("  1.New Two-Player Games")
        print("  2.Exit")
    elif choice==1 :
        make_list(total_row)
        count=0
        while result!="over" :
            if count%2!=0 :
                piece="X"
            else :
                piece="O"
            choice2=input("Player 1, enter a column(A-G) :").upper()
                #choice2 is designed for players to choose which column to put chess pieces
            column=10086
            if(choice2=="A"):
                column=0
            if(choice2=="B"):
                column=1
            if(choice2=="C"):
                column=2
            if(choice2=="D"):
                column=3
            if(choice2=="E"):
                column=4
            if(choice2=="F"):
                column=5
            if(choice2=="G"):
                column=6
            count_element=5
            #count_element is used for deciding the row
            while count_element>=0 :
                if column_judgement(column)=="right" :
                    if Spillover_judgment(total_row,column)=="not_full"  :
                        
                        if total_row[count_element][column]=="X" or total_row[count_element][column]=="O" :
                            count_element-=1
                            continue
                        
                        elif total_row[count_element][column]!="X" and total_row[count_element][column]!="O" :
                            total_row[count_element][column]=piece
                            count_element-=1
                            make_list(total_row)
    
                            judgement,winner=Judge_the_victory(total_row)
                            if judgement=="finished" :
                                result="over"
                                resu1_winner=winner
                            break
                           
                    elif Spillover_judgment(total_row,column)=="full" :
                        print("The column is full, please select another column")
                        count-=1
                        break

                elif column_judgement(column)=="wrong" :
                    print("This column is not optional, please select another column")
                    count-=1
                    break
            count+=1
    print(resu1_winner,"wins!")
game()