########-------- This Is Conversion of Finite Automata ----->>>>> Regular Expression............##############


################################# Conversion of FA to RE Contains 4 Steps ####################################

# -> STEP_1 : If there are more than 1 initial states than convert them into 1 initial states
# -> STEP_2 : If there are more than 1 final states than conver them into 1 final state
# -> STEP_3 : If we move from one state to another with more than 1 transition elements than combine them with + operator
# -> Step_4 : If there are 3 consecutive states than remove middle one and directly combine first and third state by concatenation



## This Function takes input FA from user 
def get_transition_table():
    #Empty dictionary to store transition table
    transition_table = {}
    while True:
        print("Enter the state name or 'stop' to exit:")
        state = input()
        if state == "stop":
            break
        transition_table[state] = {}
        print("Enter the transition for alphabets separated by space:")
        alphabets = input().split()
        for alphabet in alphabets:
            print("Enter next state for alphabet",alphabet,":")
            next_state = input()
            transition_table[state][alphabet] = next_state
    return transition_table

transition_table = get_transition_table()
print(transition_table)

# This function will convert dictionary keys to values and vice versa and concatenate repeatetive value keys

def flip_dict(To_be_flipped):
    flipped = {}                
    for key, value in To_be_flipped.items():
        if value not in flipped:
            flipped[value] = key
        else:
            flipped[value] = flipped[value] + '+' + key
    return flipped 

def STEP_THREE(TT):    
    for i in TT:
        new_dict = flip_dict(TT[i])
        new_dict = flip_dict(new_dict)
        TT[i] = new_dict
    return TT

transition_table = STEP_THREE(transition_table)
print(transition_table)