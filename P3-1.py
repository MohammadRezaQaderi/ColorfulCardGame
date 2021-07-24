from copy import copy, deepcopy
from typing import Tuple
Generated = 0
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

def check_heuristic(node):
    hit = 0
    for i in range(len(node)):
        if(len(node[i]) == 0):
            break
        if(not check_color(node[i]) or not check_sorted(node[i])):
                hit+=1
    return hit

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

def check_in_ex_or_fro(Child , frontier ,explored):
    flag_ex = True
    flag_fro = True
    for i in range(len(explored)):
        if(Child[0] == explored[i][0]):
            flag_ex = False
            return False
    for i in range(len(frontier)):
        if(Child[0] == frontier[i][0]):
            flag_fro = False
            return False
    return flag_fro and flag_ex

# Make the Child of Nodes
def Child_Node(frontier , explored , Num_col , Max_num):
    frontier.sort(key = lambda x:x[1] ,reverse =False)
    first = frontier[0][1]
    frontier.sort(key = lambda x:x[1] ,reverse =True)
    second = frontier[0][1]
    if(first > second):
        frontier.sort(key = lambda x:x[1] ,reverse =False)
    else:
        frontier.sort(key = lambda x:x[1] ,reverse =True)
    state = frontier[0]
    internal_frontier = []
    explored.append(state)
    flag = 0
    father_cost = frontier[0][1]
    global depth
    global Generated 
    del frontier[0]
    for i in range(len(state[0])):
        if(len(state[0][i]) == 0 and flag == 0):
                break
        else:
            chosen_card_number , chosen_card_color = split_card(state[0][i][len(state[0][i])-1])
            for j in range(len(state[0])):
                if(i == j):
                    continue
                Child = deepcopy(state)
                if(len(Child[0][j]) == 0 and flag == 0):
                    card = concat_card(chosen_card_number , chosen_card_color)
                    Child[0][i].pop(len(Child[0][i])-1)
                    Child[0][j].append(card)
                    Child[1] =int(father_cost) + int(check_heuristic(Child[0]))
                    if(check_in_ex_or_fro(Child , frontier , explored)):
                        Generated = Generated + 1
                        internal_frontier.append(Child)
                        if(goal(Child[0] , Num_col)):
                            flag = 1
                            return frontier , flag
                if(len(Child[0][j]) != 0):
                    number_of_card , color_of_card = split_card(Child[0][j][len(state[0][j])-1])
                if(number_of_card > chosen_card_number and len(Child[0][i]) != 0 and flag == 0):
                    card = concat_card(chosen_card_number , chosen_card_color)
                    Child[0][i].pop(len(Child[0][i])-1)
                    Child[0][j].append(card)
                    Child[1] =int(father_cost) + int(check_heuristic(Child[0]))
                    if(check_in_ex_or_fro(Child , frontier , explored)):
                        internal_frontier.append(Child)
                        Generated = Generated + 1
                        if(goal(Child[0] , Num_col)):
                            flag = 1
                            return frontier , flag
    for i in range(len(internal_frontier)):
        frontier.append(internal_frontier[i])
    return frontier , flag
# BFS Algorithm to Find Goal
def BFS(initial_state , Num_col , Max_num):
    state = deepcopy(initial_state)
    if(goal(state ,Num_col)):
        return state
    explored = []
    frontier = []
    frontier.append([state , check_heuristic(state)])
    flag = 0
    while True:
        if not frontier:
            return False
        frontier , flag = Child_Node(frontier , explored , Num_col , Max_num)
        if(flag == 1):
            return(print("Goal is :" +str(frontier[len(frontier) - 1]) + str(len(frontier)) +  "\nGenerated Nodes:  " + str(Generated)+"\nExpanded Nodes:  " +str(len(explored))))




k = input("Enter the col :")
m = input("Enter Num of color :")
n = input("Enter Num of each Color :")

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


BFS(initial_State , k , n)
