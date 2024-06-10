import random
import numpy as np
from numpy import ndarray


class TreeNode:
    def __init__(self, pos_X: float, pos_Y: float):
        self._pos_X: float = pos_X
        self._pos_Y: float = pos_Y
        self._children: list[float] = []
        self._parent: TreeNode | None = None


class RRTAlgorithm:
    def __init__(
        self,
        start: TreeNode,
        goal: TreeNode,
        num_iter: int,
        grid: int,
        step_size: int,
    ):
        self._rand_tree: TreeNode = TreeNode(1.1, 1.1)
        self._goal: TreeNode = TreeNode(1.1, 1.1)
        self._nearest_node: TreeNode | None = None
        self._iterations: int = min(num_iter, 200)
        self._grid: ndarray[int, int] = grid
        self._rho: int = step_size
        self._path_dist: int = 0
        self._nearest_dist: int = 10_000
        self._num_waypoints: int = 0
        self._waypoints: list[int] = []

    def add_child(self, pos_X: float, pos_Y: float) -> None:
        """
        Add the point to the nearest node and add goal when reached.
        """
        pass

    def sample_point(self):
        """
        Sample random point within limits of the grid.
        """
        pass

    def steer_to_point(self, start_loc: int, end_loc: int):
        """
        Steer a distance step_size from start to end location.
        """
        pass

    def nearest_node(self, root: TreeNode, point: int):
        """
        Find nearest node from a given unconnected point (using Euclidean distance).
        """
        pass

    def euclidean(self, node: TreeNode, point: int) -> int:
        """
        Calculate Euclidean distance between a node and an XY-coordinate.
        """
        pass

    def is_in_obstacle(self, start_loc: int, end_loc: int) -> bool:
        """
        Does an obstacle lie between start node and endpoint of the edge.
        """
        pass

    def is_goal(self, point: int) -> bool:
        """
        Check if the goal has been reached.
        """
        pass

    def reset_nearest(self) -> None:
        """
        Reset the nearest node and nearest distance.
        """
        pass

    def backtrack_path(self, goal: TreeNode):
        """
        Retrace the path from goal to start.
        """
        pass
