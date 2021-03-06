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

class Node():
    # Makes accesses idomatic, holds state of a cell in maze
    def __init__(self, state, path, priority):
        self.state = state
        self.path = path
        self.priority = priority

def genSearch(problem, container):

    # Container holds nodes which contain state
    container.push(Node(problem.getStartState(), [], 0))

    # Using list instead of set to provide comparison function for state object
    visited = []

    while not container.isEmpty():
        curr_node = container.pop()

        # to prevent needless expansion
        if curr_node.state in visited:
            continue

        visited.append(curr_node.state)

        # Done
        if problem.isGoalState(curr_node.state):
            return curr_node.path

        # Process all potential nodes
        for tup in problem.getSuccessors(curr_node.state):
            if tup[0] not in visited:
                # concat creates new path without affecting path
                container.push(Node(tup[0], curr_node.path + [tup[1]], tup[2] + curr_node.priority))

    raise RunTimeError("Exausted search space, but found no goal")

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
    """ Search the deepest nodes in the search tree first. """
    return genSearch(problem, util.Stack())

def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    return genSearch(problem, util.Queue())

def uniformCostSearch(problem):
    """Search the node of least total cost first."""

    # lambda of cost function since costFn expecting coord
    priority_queue = util.PriorityQueueWithFunction(lambda x: x.priority)
    return genSearch(problem, priority_queue)

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """ Search the node that has the lowest combined cost and heuristic first."""
    priority_queue = util.PriorityQueueWithFunction(lambda x: x.priority + heuristic(x.state, problem))
    return genSearch(problem, priority_queue)


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch