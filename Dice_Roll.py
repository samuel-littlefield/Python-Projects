from random import randint

def dice_roll():
    
    dice_drawing = {  
    1: (  
        "┌─────────┐",  
        "│         │",  
        "│    ●    │",  
        "│         │",  
        "└─────────┘",
    ),  
    2: (  
        "┌─────────┐",  
        "│    ●    │",  
        "│         │",  
        "│    ●    │",  
        "└─────────┘",
    ),  
    3: (  
        "┌─────────┐",  
        "│ ●       │",  
        "│    ●    │",  
        "│       ● │",  
        "└─────────┘",  
    ),  
    4: (  
        "┌─────────┐",  
        "│ ●     ● │",  
        "│         │",  
        "│ ●     ● │",  
        "└─────────┘",
    ),  
    5: (  
        "┌─────────┐",  
        "│ ●     ● │",  
        "│    ●    │",  
        "│ ●     ● │",  
        "└─────────┘",  
    ),  
    6: (  
        "┌─────────┐",  
        "│ ●     ● │",  
        "│ ●     ● │",  
        "│ ●     ● │",  
        "└─────────┘",  
    ),  
                    } 
    
    roll = input("Roll the dice? (Yes/No): ")
    
    while roll.lower() == "Yes".lower():
        dice1 = randint(1, 6)
        dice2 = randint(1, 6)
        
        print("dice rolled: {} and {}".format(dice1, dice2))
        print("\n".join(dice_drawing[dice1]))
        print("\n".join(dice_drawing[dice2]))
        
        roll = input("Roll again? (Yes/No): ")
        
dice_roll()