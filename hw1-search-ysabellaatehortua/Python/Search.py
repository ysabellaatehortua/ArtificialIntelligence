"""
Search.py runs various search algorithms on
the same map to find the fastest path

Ysabella Atehortua
10/24/2021
"""
import map
import problem
import sys
import time
from operator import itemgetter, attrgetter
import numpy as np
import math

#get_path returns the path length from any state to the start state
def get_path(state, start):
    path = 0
    cost = 0
    #print(start)
    while state[2] != start: #while previous doesn't equal start
        path += 1
        cost += state[1]
        #print(cost)
        #print(state[1])
        state = state[2]
    return [path, cost]

#check_child checks if a state is in explored or frontier and adds it to the frontier if not.
def checkchild(frontier, explored, child, prev, problem_model):
    if child not in explored:
        if child not in frontier:
            #print(prev)
            #print(child)
            child = [child, bfscost(problem_model, prev, child), prev] #change child to convention
            frontier.append(child)
            return

#returns the cost of an action on a node
#(kind of a redundant function, error checks, scared to remove incase code breaks)
def bfscost(problem_model, previous, state):
#    print(state == previous[0])
    #print(state)
    #print(previous[0])
    #print(previous)
    if previous[0] == state:
        return 0
    else:
        #print(previous[0])
        #print(state)
        #print()
        #print(problem.Problem.cost(problem_model, previous[0], state))
        return problem.Problem.cost(problem_model, state, previous[0])

#main function to run breadth first search on a map given a start state
def bfs(start, problem_model): #function for BFS
    startTime = time.process_time()
    frontier = []
    explored = []
    expanded = 0
    cost = 0
    start = [start, cost, start]
    frontier.append(start)
    prev = start
    #print(prev)
    while len(frontier) > 0:
             # Creating loop to visit each node
        state = frontier.pop()
        #print(prev)
        #print(state)
        #state = [state[0], bfscost(problem_model, prev, state[0]), prev]
        #print(state)
        explored.append(state[0])
        #add the head's children to the tree
        for child in problem.Problem.actions(problem_model, state[0]):
            expanded += 1
            #print(child)
            if problem.Problem.goal(problem_model, child):
                #print(prev)
                endTime = time.process_time()
                duration = endTime - startTime
                #print(state)
                #print(child)
                goal = [child, bfscost(problem_model, state, child), state]
                path = get_path(goal, start)
                #print(path)
                print("BFS Path Length: ", path[0]) #length of Path
                print("BFS Path Cost: ", path[1]) #cost of Path
                print("BFS Goal Reached: ", child)
                print("Nodes Expanded with BFS: ", expanded)
                print("Time Spent with BFS: ", duration)
                return
            #print(prev)
            checkchild(frontier, explored, child, state, problem_model)
            #print(prev)
        prev = state
        #print(prev)

#returns the path length of UCS algorithm
def ucs_path(problem_model, goal, start):
    current = goal
    path = 0
    cost = 0
    while current != start:
        path += 1
        cost += current[1]
        current = current [2]
    return [path, cost]

#main function for UCS algorithm given a map and start state
def  uniform_cost_search(start, problem_model):
    startTime = time.process_time()
    frontier = []
    explored = []
    expanded = 0
    cost = 0
    start = [start, cost, start]
    #prev = start
    frontier.append(start)
    while len(frontier) > 0:          # Creating loop to visit each node
        state = frontier.pop()
        #print(state)
        #state = [state, bfscost(problem_model, prev, state), prev]
        #print(state)
        if problem.Problem.goal(problem_model, state[0]):
            endTime = time.process_time()
            duration = endTime - startTime
            #print(child)
            path = ucs_path(problem_model, state, start)
            #print(path)
            print("UCS Path Length: ", path[0]) #length of Path
            print("UCS Path Cost: ", path[1]) #cost of Path
            print("UCS Goal Reached: ", state[0])
            print("Nodes Expanded with UCS: ", expanded)
            print("Time Spent with UCS: ", duration)
            return state
        #print(prev[0])
        #print(state[0])
        #state = [state, bfscost(problem_model, prev, state[0]), prev]
        #print(state)
        explored.append(state[0])
        for child in problem.Problem.actions(problem_model, state[0]):
            expanded += 1
            if child not in explored:
                if child not in frontier:
                    child = [child, problem.Problem.cost(problem_model, state[0], child), state]
                    frontier.append(child)
                    #print(frontier)
                    frontier = sorted(frontier, key=itemgetter(1))
                elif child in frontier:
                    index = frontier.index(child)
                    #print(index)
                    if child[1] < frontier[index][1]:
                        frontier = [child if i==index else i for i in frontier]
                        frontier = sorted(frontier, key=itemgetter(1))
        #print(state)
        #prev = state

#calculates heuristic cost given two states
def heuristic(start, child2):
    dist = math.sqrt((child2[0] - start[0])**2 + (child2[1] - start[1])**2)
    return dist

#calculate cost from node to nearest goal state
def find_togo(state, problem_model):
    togo = 100**99
    for goal in problem.Problem.goalStates(problem_model):
        if heuristic(state, goal) < togo:
            togo = heuristic(state, goal)
    #print(togo)
    return togo

#calculates path length for A* algorithm
def findPath(goal, start):
    path = 1
    while goal[3] != start:
        goal = goal[3]
        path += 1
    return path

#driver function for A* given a map and start node
def a_star_algorithm(start, problem_model):
    startTime = time.process_time()
    frontier = []
    start_to_finish = find_togo(start, problem_model)
    start = [start, 0, start_to_finish, start]
    frontier.append(start)
    explored = []
    expanded = 0
    while len(frontier) > 0:   # Creating loop to visit each node
        state = frontier.pop(0)
        expanded += 1
        if state[0] in problem.Problem.goalStates(problem_model):
            endTime = time.process_time()
            duration = endTime - startTime
            path = findPath(state, start)
            print("A* Path Length: ", path) #length of Path
            print("A* Path Cost: ", state[1]) #cost of Path
            print("A* Goal Reached: ", state[0])
            print("Nodes Expanded with A*: ", expanded)
            print("Time Spent with A*: ", duration)
            return
        if state[0] not in explored:
            explored.append(state[0])
        #print(explored)
    #    print(problem.Problem.actions(problem_model, state[0]))
        for child in problem.Problem.actions(problem_model, state[0]):
            togo = find_togo(child, problem_model)
            sofar = math.sqrt((child[0] - start[0][0])**2 + (child[1] - start[0][1])**2)
            child = [child, sofar, togo, state]
        #    print(child[0])
            if child[0] not in explored:
                if child[0] not in frontier:
                    frontier.append(child)
                    frontier = sorted(frontier, key=itemgetter(2))
                elif child in frontier:
                    index = frontier.index(child)
                    if find_togo(child, problem_model) < find_togo(frontier[index], problem_model):
                        frontier[index] = child
                        frontier = sorted(frontier, key=itemgetter(2))


def main():
    filename = sys.argv[1]
    my_map = map.readFromFile(filename)
    problem_model = problem.Problem(my_map)
    start = problem.Problem.startState(problem_model)
    bfs(start, problem_model)
    print()
    uniform_cost_search(start, problem_model)
    print()
    a_star_algorithm(start, problem_model)

main()
