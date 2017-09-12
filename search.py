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
from sets import Set
import util
import random

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
    return [s, s, w, s, w, w, s, w]

class Node(object):
    def __init__(self):
        self.state=None
        self.solution=[]
        self.cost=0

    def __eq__(self, other):
        return self.state == other.state and self.parent == other.parent and self.cost == other.cost

def depthFirstSearch(problem):
    node = Node()
    node.state=problem.getStartState()
    frontier=util.Stack()
    frontier.push(node)
    explored=Set([])

    while True:
        if frontier.isEmpty():
            return []
        node=frontier.pop()
        if problem.isGoalState(node.state):
            return node.solution

        explored.add(node.state)

        for action in problem.getSuccessors(node.state):
            child=Node()
            child.cost=node.cost + action[2]
            child.solution=list(node.solution)
            child.solution.append(action[1])
            child.state=action[0]
            if not (child.state) in explored:
                frontier.push(child)


def depthFirstSearchReversed(problem):
    node = Node()
    node.state=problem.getStartState()
    frontier=util.Stack()
    frontier.push(node)
    explored=Set([])

    while True:
        if frontier.isEmpty():
            return []
        node=frontier.pop()
        if problem.isGoalState(node.state):
            return node.solution

        explored.add(node.state)

        successors = problem.getSuccessors(node.state)
        
        for action in reversed(successors):
            child=Node()
            child.cost=node.cost + action[2]
            child.solution=list(node.solution)
            child.solution.append(action[1])
            child.state=action[0]
            if not (child.state) in explored:
                frontier.push(child)

def dummySearch(problem):
    return []

def breadthFirstSearch(problem):
    node = Node()
    node.state=problem.getStartState()
    frontier=util.Queue()
    frontier.push(node)
    explored=Set([])

    while True:
        if frontier.isEmpty():
            return []
        node=frontier.pop()
        if problem.isGoalState(node.state):
            return node.solution

        explored.add(node.state)

        successors = problem.getSuccessors(node.state)
        random.shuffle(successors)
        for action in successors:
            child=Node()
            child.cost=node.cost + action[2]
            child.solution=list(node.solution)
            child.solution.append(action[1])
            child.state=action[0]
            if not (child.state) in explored:
                frontier.push(child)



def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
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
dfsR = depthFirstSearchReversed