# TA_PROJECT
I developed a Code for converting Finite Automata into Regular Expression in Python using dictionaries.
This was my course project and it contains some specific terms that comes from the course Theory Of Automata AKA Theory of Computation

################################# Conversion of FA -> RE Contains 4 Steps ####################################

# -> STEP_1 : If there are more than 1 initial states than convert them into 1 initial states
# -> STEP_2 : If there are more than 1 final states than conver them into 1 final state
# -> STEP_3 : If we move from one state to another with more than 1 transition elements than combine them with + operator
# -> Step_4 : If there are 3 consecutive states than remove middle one and directly combine first and third state by concatenation
