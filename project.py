########-------- This Is Conversion of Finite Automata ----->>>>> Regular Expression............##############


################################# Conversion of FA to RE Contains 4 Steps ####################################

# -> STEP_1 : If there are more than 1 initial states than convert them into 1 initial states
# -> STEP_2 : If there are more than 1 final states than conver them into 1 final state
# -> STEP_3 : If we move from one state to another with more than 1 transition elements than combine them with + operator
# -> Step_4 : If there are 3 consecutive states than remove middle one and directly combine first and third state by concatenation


## This Function takes input FA from user 
def GetTransitionTable():
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



# This function will convert dictionary keys to values and vice versa and concatenate repeatetive value keys

def FlipDict(To_be_flipped):
    flipped = {}                
    for key, value in To_be_flipped.items():
        if value not in flipped:
            flipped[value] = key
        else:
            flipped[value] = '(' + flipped[value] + '+' + key + ')'
    return flipped 

def StepThree(TT):              # TT Stands for Transitions Table
    for i in TT:
        new_dict = FlipDict(TT[i])
        new_dict = FlipDict(new_dict)
        TT[i] = new_dict
    return TT

def StepFour(TT,S_to_E):
    TT = ConCatNodes(InComingStates(TT,S_to_E),TT,S_to_E)
    TT = DelState(TT,TT[S_to_E])    
    return TT


def DelState(TT,S_to_E):         ## State to be eliminated from the dictionary
    rem_tt = {}                  ## Remaining Transition Table
    S_to_E.clear()               ## Deleting The state values
    
    for key,value in TT.items():
        if value == {}:
            continue             ## Just Do Nothing and do not save its Key
        else:
            rem_tt[key] = value
    return rem_tt

def InComingStates(TT,S_to_E):          ## This function will track those nodes which are coming to S_to_E
    NodesArr = []
    
    for i in TT:
        for j in TT[i]:
            if TT[i][j] == S_to_E:
                NodesArr.append(i)
    return NodesArr

def CheckSelfLoop(TT,S_to_E):
    for j in TT[S_to_E]:
        if TT[S_to_E][j] == S_to_E:
            return '(' + j + ')*'            
    return ''

def ConCatNodes(CmingStates,TT,S_to_E):  ## In This function we are concatenating nodes(1->2->3) will become (1->3)
    for i in CmingStates:
        updated_dict = {}
        
        for key in TT :
            if key == i:
                for val in TT[key]:
                    if TT[key][val] == S_to_E :
                        updated_key = {}
                        
                        for GST in TT[S_to_E]:          ## GST(Going State Transition means that transition element by which we are going to some next state)
                            updated_key['(' + val + CheckSelfLoop(TT,S_to_E) + GST + ')'] = TT[S_to_E][GST]
                        updated_dict[key] = updated_key
            else:
                updated_dict[key] = TT[key]
        TT = updated_dict
    return TT

# Main Environment
 

dict = {'x1':{'a':'x2','b':'x2'},'x2':{'b':'x3','a':'x2'},'x3':{'c':'x4'},'x4':{'a':'x5'},'x5':{'e':'x5'}}

ini = 'x1'
final = 'x5'


for i in dict.keys():
    if(i != ini and i != final):
        dict = StepThree(dict)
        dict = StepFour(dict,i)    
        
    
print(dict)