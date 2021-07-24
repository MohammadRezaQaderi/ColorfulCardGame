from copy import copy, deepcopy
from typing import get_args
 
Generated = 1
#  the func split the card name 
def split_card(x):
    return int(x[0]) ,str(x[1])

# Concatenating the number and color to make card
def concat_card(number , color):
    return str(number)+color

# this is for check is the cards number was sorted :)
def check_sorted(number_card):
    flag = 0
    test_number_card = number_card[:]
    # test_number_card.sort()
    test_number_card.sort(reverse = True)
    if(len(number_card) == 0):
        flag = 0
    if (test_number_card == number_card):
        flag = 1
    if(flag):
        return True
    else:
        return False

# this is for check is all element is same :))
def check_color(color_card):
    flag = 0
    if(len(color_card) == 0):
        flag = 0 
    if len(color_card) >0 :
        flag = all(element == color_card[0] for element in color_card)
    if(flag):
        return True
    else:
        return False

# this check each col is ok or no 
def check_foreach_col(colors , numbers):
    if (check_sorted(numbers) and check_color(colors)):
        return True
    else:
        return False

# this function was for check for are weon goal state :|
def goal(state , Num_col):
    flag = 0
    for j in range(len(state)):
        number_of_cards = []
        color_of_cards = []
        if(len(state[j]) == 0 ):
                flag = flag + 1 
                continue
        for i in range(len(state[j])):
            number_of_card , color_of_card = split_card(state[j][i])
            number_of_cards.append(number_of_card)
            color_of_cards.append(color_of_card)
        if (check_foreach_col(color_of_cards , number_of_cards)):
            flag = flag + 1
    if (flag == int(Num_col)):
        return True
    else:
        return False

# Make the Child of Nodes
def Child_Node(frontier , explored , Num_col , limit):
    global Generated
    flag = 0
    for k in range(len(frontier)):
        state = frontier[0]
        internal_frontier = []
        explored.append(state)
        del frontier[0]
        for i in range(len(state)):
            if(len(state[i]) == 0 and flag == 0):
                    break
            chosen_card_number , chosen_card_color = split_card(state[i][len(state[i])-1])
            for j in range(len(state)):
                if(i == j):
                    continue
                Child = deepcopy(state)
                if(len(Child[j]) == 0 and flag == 0):
                    card = concat_card(chosen_card_number , chosen_card_color)
                    Child[i].pop(len(Child[i])-1)
                    Child[j].append(card)
                    # Generated = Generated + 1
                    if(Child not in explored and Child not in frontier):
                        Generated = Generated + 1
                        internal_frontier.insert( 0 , Child)
                    if(goal(Child , Num_col)):
                        flag = 1
                        for i in range(len(internal_frontier)):
                            frontier.append(internal_frontier[len(internal_frontier) - i - 1])
                        return frontier , flag 
                if(len(Child[j]) != 0):
                    number_of_card , color_of_card = split_card(Child[j][len(state[j])-1])
                if(number_of_card > chosen_card_number and len(Child[i]) != 0 and flag == 0):
                    card = concat_card(chosen_card_number , chosen_card_color)
                    Child[i].pop(len(Child[i])-1)
                    Child[j].append(card)
                    # Generated = Generated + 1
                    if(Child not in explored and Child not in frontier):
                        Generated = Generated + 1
                        internal_frontier.insert( 0 , Child)
                    if(goal(Child , Num_col)):
                        flag = 1
                        for i in range(len(internal_frontier)):
                            frontier.append(internal_frontier[len(internal_frontier) - i - 1])
                        return frontier , flag
        for i in range(len(internal_frontier)):
            frontier.append(internal_frontier[len(internal_frontier) - i - 1])
    return frontier , flag 

# Depth limited search DLS 
def DLS(initial_state , limit , Num_col): 
    return recursive_Dls( initial_state , limit , Num_col)

def recursive_Dls(initial_state , limit , Num_col):
    explored = []
    frontier = []
    global Generated
    frontier.append(initial_state)
    if(limit == 0):
        if(goal(initial_state , Num_col)):
            return initial_state , 1 , 0
        else:
            return initial_state , 0 , 0 
    else:
        flag = 0
        for i in range(int(limit)):
            frontier , flag = Child_Node(frontier , explored , Num_col , limit)
            if(flag == 1):
                return frontier[len(frontier)-1] , flag , i
        return [] , flag , 0


def itrative_deepening_search(initial_state, limit , Num_col):
    goal = []
    global Generated
    while True: 
        goal , flag , cutoff = DLS(initial_state , limit ,Num_col)
        limit = limit + 1
        if (flag == 1):
            return  (print("Goal is :" ,(goal),  "\nGenerated Nodes:  " , Generated ,  "\nSolution Depth:  " , (cutoff+1) ))


k = input("Enter the col :")
m = input("Enter Num of color :")
n = input("Enter Num of each Color :")
limit = int(input("Enter First Limit :"))


initial_State = []
count = 0
while  count < int(k):
    x = list(map(str,input().split()))
    if x[0] == '#':
        x = list()
        initial_State.append(x)
        count = count+1
        continue
    initial_State.append(x) 
    count = count+1

itrative_deepening_search(initial_State , limit , k)
