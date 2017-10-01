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

    def create_child(self, state, addSolution, addCost):
        child = Node()
        child.state = tuple(state)
        child.solution = list(self.solution)
        child.solution.append(addSolution)
        child.cost = self.cost + addCost
        return child

   
def depthFirstSearch(problem):
    node = Node()
    node.state=problem.getStartState()
    frontier=util.Stack()
    frontier.push(node)
    explored=set()

    while True:

        if frontier.isEmpty():
            print "No hay solucion"
            return []

        node = frontier.pop()

        if node.state in explored:
            continue
            
        if problem.isGoalState(node.state):
            return node.solution

        explored.add(node.state)

        for action in problem.getSuccessors(node.state):
            child = node.create_child(action[0], action[1], action[2])

            if not child.state in explored:
                frontier.push(child)

def breadthFirstSearch(problem):
    node = Node()
    node.state=problem.getStartState()
    frontier=util.Queue()
    frontier.push(node)
    explored=set()
    while True:

        if frontier.isEmpty():
            print "No hay solucion"
            return []

        node=frontier.pop()

        # Debido a que no se puede checkear la frontera al momento de insertar el nodo
        # se debe checkear en este punto si el estado del nodo sacado ya ha sido 
        # explorado o no 
        if node.state in explored:
           continue

        explored.add(node.state)

        for action in problem.getSuccessors(node.state):
            child = node.create_child(action[0], action[1], action[2])

            # La clase Queue que se da no tiene una funcion para checkear si ya hay un elemento en ella
            if not child.state in explored:
                if problem.isGoalState(child.state):
                    return child.solution
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