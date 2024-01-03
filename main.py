import random
MAX_LINES=3 # constant value that will not change
MAX_BET=100
MIN_BET=1
ROWS=3
COLS=3
count_for_symbol={
    "A":2,
    "B":4,
    "C":6,
    "D":8
}
value_for_symbol={
    "A":5,
    "B":4,
    "C":3,
    "D":2
}
def check_winnings(columns,lines,bet,values):
    winnings=0
    winning_lines=[]
    for line in range(lines):
        symbol=columns[0][line]
        for column in columns:
            symbol_to_check=column[line]
            if symbol != symbol_to_check:
                break
        else:
            winnings += values[symbol] * bet
            winning_lines.append(line+1)
    return winnings,winning_lines
        
        
    
    
def get_slot_machine_spinning(rows,cols,symbols):
    all_symbols=[]
    for symbol,count_for_symbol in symbols.items():
        for _ in range(count_for_symbol):
            all_symbols.append(symbol)
    columns=[]
    
    for col in range(cols):
        column=[]
        current_symbols=all_symbols[:]# copying
        for row in range(rows):
            value=random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)  # Fix: Append the value to the column, not columns
        columns.append(column)  # Fix: Append the column to columns
    return columns

def printing_slot_machine(columns):
    # [A,B,C]
    # [A,B,C]
    # [A,B,C]
    #doing something like above maybe??
    for row in range(len(columns[0])):#for every single loopi we loop for every single row this essentially transposes our columns
        for i,column in enumerate(columns):
            if i != len(columns)-1:
                print(column[row],end="|")
            else:
                print(column[row],end="")
        print()
                
            

    
def deposit():
    ## se we wrote a function deposit  here we ask what is the amount then wwe wcheck if the amount is digit then we will convert it into the int 
    #then we put the conditions for greater than 0 or lesss than 0
    
    while True:
        amount=input("what would you like to deposit ?  $ ")
        if amount.isdigit():#will tell us if this is a valid number 
            amount=int(amount) #will convert the string command into the string 
            if amount>0:
                break
            else:
                print("amount must be greater than 0")
        else:
            print("please enter a number.")
        
    return amount

def get_number_of_lines():
    while True:
        lines=input("Enter the number of the lines to bet on (1-" + str(MAX_LINES)+ ")? ")
        if lines.isdigit(): 
            lines=int(lines) 
            if 1<=lines <= MAX_LINES:
                break
            else:
                print("Enter a valid number of lines")
        else:
            print("please enter a number.")
        
    return lines    

def get_bet():
    while True:
        amount=input("what would you like to bet on each line ?  $ ")
        if amount.isdigit():#will tell us if this is a valid number 
            amount=int(amount) #will convert the string command into the string 
            if MIN_BET <= amount <=MAX_BET:
                break
            else:
                print(f"amount must be between ${MIN_BET} - ${MAX_BET}.")
                
        else:
            print("please enter a number.")
        
    return amount
    

def spin(balance):
    balance=deposit()
    lines=get_number_of_lines()
    while True:
        
        bet=get_bet()
        total_bet= bet * lines
        
        if total_bet>balance:
            print(f"you do not have anough to bet that amount, your current balance is : ${balance}  ")
        else:
            break    
    print(f"you are betting on ${bet} on ${lines} lines. total bet is equal to: $ ${total_bet}")
    slots=get_slot_machine_spinning (ROWS,COLS,count_for_symbol)
    printing_slot_machine(slots)
    winnings,winning_lines= check_winnings(slots,lines,bet,value_for_symbol)
    print(f"you won${winnings}")
    print(f"you won on lines :$", *winning_lines)
    return winnings - total_bet
# def spin():
#     balance = deposit()
#     lines = get_number_of_lines()
#     while True:
#         bet = get_bet()
#         total_bet = bet * lines
#         if total_bet > balance:
#             print(f"you do not have enough to bet that amount, your current balance is: ${balance}")
#         else:
#             break
#     print(f"you are betting on ${bet} on {lines} lines. Total bet is equal to: ${total_bet}")
#     slots = get_slot_machine_spinning(ROWS, COLS, count_for_symbol)
#     printing_slot_machine(slots)
#     winnings, winning_lines = check_winnings(slots, lines, bet, value_for_symbol)
#     print(f"you won ${winnings}")
#     print("you won on lines:", *winning_lines)
#     return sum(winning_lines) - total_bet
    
      
def main():
    balance=deposit()
    while True:
        print(f"current balance is ${balance}")
        answer=input("press enter to spin (q to exit)")
        if answer == "q":
            break
        balance +=spin(balance)
        
    print(f"you left ith balance {balance}")


main()    