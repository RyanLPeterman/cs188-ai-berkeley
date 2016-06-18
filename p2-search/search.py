# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
#
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print "Start:", problem.getStartState()
    print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    print "Start's successors:", problem.getSuccessors(problem.getStartState())
    """

    # list of actions leading to goal
    actions = []
    visited_set = set()

    stack = util.Stack()
    stack.push((problem.getStartState(), None, 1))

    while not stack.isEmpty():

        curr = stack.pop()
        visited_set.add(curr[0])
        if curr[1]:
            actions.append(curr[1])

        # import sys
        # sys.stdin.readline()
        # print "Curr:", curr[0]
        # print "Curr's successors:", problem.getSuccessors(curr[0])
        # print "Stack: ", stack._print()
        # print curr[1]

        # Done
        if problem.isGoalState(curr[0]):
            return actions


        # Dead End
        is_dead_end = True

        # Process all potential nodes
        for node in problem.getSuccessors(curr[0]):
            if not node[0] in visited_set:
                is_dead_end = False
                stack.push(node)

        if is_dead_end:
            # Pop actions until state is restored to last node on stack
            curr_state = curr[0]
            goal_state = stack.top()[0]

            while goal_state not in [coord[0] for coord in problem.getSuccessors(curr_state)]:
                prev_action = actions.pop()
                delta_x = 0
                delta_y = 0

                if prev_action == 'North':
                    delta_y = -1
                elif prev_action == 'South':
                    delta_y = 1
                elif prev_action == 'East':
                    delta_x = -1
                elif prev_action == 'West':
                    delta_x = 1
                else:
                    raise Exception('Invalid Direction Found')

                curr_state = (int(curr_state[0]) + delta_x, int(curr_state[1]) + delta_y)


    print "Exausted search space, but found no goal"
    return actions

def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    util.raiseNotDefined()

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    priority_queue = util.PriorityQueue()

    util.raiseNotDefined()

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch