[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-f059dc9a6f8d3a56e377f745f24479a46679e63a5d9fe6f495e02850cd0d8118.svg)](https://classroom.github.com/online_ide?assignment_repo_id=6029606&assignment_repo_type=AssignmentRepo)
# hw1-search
HW1: Search for a Restaurant

Credit to OpenStreetMaps.com for the data used to generate the maps used in this assignment.

# Your Answers Go Here #
1. 
mapT.dat
BFS Path Length:  3
BFS Path Cost:  4.0
BFS Goal Reached:  (8.0, 5.0)
Nodes Expanded with BFS:  9
Time Spent with BFS:  2.9000000000001247e-05

UCS Path Length:  4
UCS Path Cost:  6.0
UCS Goal Reached:  (8.0, 5.0)
Nodes Expanded with UCS:  9
Time Spent with UCS:  2.199999999996649e-05

A* Path Length:  4
A* Path Cost:  6.0
A* Goal Reached:  (8.0, 5.0)
Nodes Expanded with A*:  5
Time Spent with A*:  6.999999999995898e-05

mapL.dat
BFS Path Length:  7050
BFS Path Cost:  4.464400000000077
BFS Goal Reached:  (40.8570488, -96.6378949)
Nodes Expanded with BFS:  40124
Time Spent with BFS:  7.341928

UCS Path Length:  460
UCS Path Cost:  0.6066999999999999
UCS Goal Reached:  (40.8570488, -96.6378949)
Nodes Expanded with UCS:  40519
Time Spent with UCS:  11.244486999999998

A* Path Length:  164
A* Path Cost:  0.05620748444299814
A* Goal Reached:  (40.7562167, -96.6529419)
Nodes Expanded with A*:  167
Time Spent with A*:  0.0047739999999976135

mapO.dat
BFS Path Length:  325
BFS Path Cost:  0.38470000000000015
BFS Goal Reached:  (41.2904548, -82.2184917)
Nodes Expanded with BFS:  1170
Time Spent with BFS:  0.007910000000000028

UCS Path Length:  117
UCS Path Cost:  0.19760000000000003
UCS Goal Reached:  (41.2904548, -82.2184917)
Nodes Expanded with UCS:  5450
Time Spent with UCS:  0.16315399999999997

A* Path Length:  64
A* Path Cost:  0.04569866928182902
A* Goal Reached:  (41.2904548, -82.2184917)
Nodes Expanded with A*:  69
Time Spent with A*:  0.0013340000000000019

mapC.dat
BFS Path Length:  1237
BFS Path Cost:  0.9422999999999939
BFS Goal Reached:  (41.483662, -81.730277)
Nodes Expanded with BFS:  5623
Time Spent with BFS:  0.169416

UCS Path Length:  420
UCS Path Cost:  0.5203999999999995
UCS Goal Reached:  (41.4843221, -81.7042646)
Nodes Expanded with UCS:  11978
Time Spent with UCS:  0.769048

A* Path Length:  192
A* Path Cost:  0.042157116205931947
A* Goal Reached:  (41.483662, -81.730277)
Nodes Expanded with A*:  520
Time Spent with A*:  0.017265000000000086

2. My algortims found most of the same goals, expect in the case of mapL, in which my A* algoritm was able to find the least costly path. The costs of the paths varied quite a bit -- which A* consistently producing the least costly paths, BFS producing the most costly, and UCS landing somewhere in the middle. The algoritms followed a similar pattern in terms of how much work they did, while A* expanding the least amount of nodes and taking the shortest amount of time, BFS expanding the most nodes and taking the longest amount of time, and UCS falling somewhere in the middle. The heuristic I used for my A* algorithm was the euclidian distance formula in which I calculated the total cost of an action based on the distance a state was from the start plus the distance to the goal. 

3. I really enjoyed this assignment. Apart from an illness that forced me to take longer on it than normally, I appreciated how much liberty I had on this assignment. The directions were clear enough that I did not question the goals -- and the pseudocode very helpful in constructing my algoritms. However, I was able to make decisions based on my own preferences, i.e., what data structures to use, how to format my nodes, what language to use, etc.

4. I estimate I spent 8/9 hours on the assignment (though it's hard to tell -- time flies when youre having fun)

5. I affirm that I have adhered to the honor code on this assignment.
