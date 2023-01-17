########--------------<<<<<<<<-------- This Is Conversion of Finite Automata ---------->>>>> Regular Expression--------------##############


################################# Conversion of FA to RE Contains 4 Steps ####################################

# -> STEP_1 : If there are more than 1 initial states than convert them into 1 initial states
# -> STEP_2 : If there are more than 1 final_state states than conver them into 1 final_state state
# -> STEP_3 : If we move from one state to another with more than 1 transition elements than combine them with + operator
# -> Step_4 : If there are 3 consecutive states than remove middle one and directly combine first and third state by concatenation



## This Function takes input FA from user 
def GetTransitionTable():
    #Empty dictionary to store transition table
    transition_table = {}
    while True:
        print("Enter the state name(for Initial use i and f for final ) or 'stop' to exit:")
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

## This function will check if there is no final state mentioned it will automatically consider initial state as final ################
def CheckFinalState(TT):    
    for key in TT:
        if key == 'f':
            return True
    return False


# This function will convert dictionary keys to values and vice versa and concatenate repeatetive value keys

def FlipDict(To_be_flipped):
    flipped = {}                
    for key, value in To_be_flipped.items():
        if value not in flipped:
            flipped[value] = key
        else:
            flipped[value] = '(' + flipped[value] + '+' + key + ')'
    return flipped 

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
    NodesArr = []                       ## All Incoming Nodes will be stored in this array
    
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

def ConCatNodes(CmingStates,TT,S_to_E):             ## In This function we are concatenating nodes(1->2->3) will become (1->3)
    for i in CmingStates:
        updated_dict = {}                           ## Empty Dictionary for States
        
        for KEY in TT :
            if KEY == i and i != S_to_E:            ## there is no benefit in checking S_to_E as it will be removed
                updated_dict[KEY] = {}              ## Empty nested dictionary for transition elements
                for Val in TT[KEY]:

                    if TT[KEY][Val] == S_to_E :     
                        for GST in TT[S_to_E]:          ## GST(Going State Transition means that transition element by which we are going to some next state)
                            
                            if TT[S_to_E][GST] == S_to_E and S_to_E != final_state :
                                continue                ## As its not a final state and we r coming back to S_to_E which simpl tells us that there is a loop of itself so no need to add it into updated dictionary 
                            else:

                                if CheckSelfLoop(TT,S_to_E) == '(' + GST + ')*':    ## IF self loop and GST are same so we have to stop them from repeatition
                                    updated_dict[KEY]['(' + Val + CheckSelfLoop(TT,S_to_E)  + ')'] = TT[S_to_E][GST]
                                else:
                                    updated_dict[KEY]['(' + Val + CheckSelfLoop(TT,S_to_E) + GST + ')'] = TT[S_to_E][GST]
                        
                    else:
                        updated_dict[KEY][Val] = TT[KEY][Val]   ## if upcomming state is different than S_to_E it will remain same as in TT
                    
            else:
                updated_dict[KEY] = TT[KEY]
        
        TT = updated_dict
    return TT

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

def GetRegEx(TT):
    TT = StepThree(TT)
    regex = ''
    print(TT)
    for key in TT[ini_state]:
        if key == '':
            return 'NULL'
        regex = regex + key
    return regex
     

#----------//////////// Main Environment \\\\\\\\\\\\\\\----------------- 

# TransitionTable = GetTransitionTable()
TransitionTable = {'i':{'a':'x1','b':'x3'},'x1':{'a':'i','b':'f'},'x3':{'a':'f','b':'i'},'f':{'b':'x1','a':'x3'}}

if(CheckFinalState(TransitionTable)):
    ini_state = 'i'
    final_state = 'f'
else:
    ini_state = 'i'
    TransitionTable['i']['null'] = 'i'
    final_state = ini_state

for i in TransitionTable.keys():
    if(i != ini_state ):
        TransitionTable = StepThree(TransitionTable)
        TransitionTable = StepFour(TransitionTable,i)  

print(GetRegEx(TransitionTable))

