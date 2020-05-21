#!/usr/bin/env python3
"""
Sultanov Andriy
MIT License 2020
"""
from btnode import Node
from copy import deepcopy
from random import shuffle


class BinaryTree:
    """
    BinaryTree for the TicTacToe game, representing a set
    of possible turns and consequent game boards
    """

    def __init__(self, starting_board, player="Player 1"):
        self._root = Node(starting_board)
        self.player = player
        self.markers = {"Player 1": "O", "Player 2": "X"}

    def create_tree(self):
        """
        Builds a binary tree of possible boards.
        Chooses two turns randomly
        """
        def recurse(node, player):
            current_board = node.board
            possible_turns = current_board.free_cells()

            if possible_turns is None:
                return None

            if len(possible_turns) == 1:
                new_board = deepcopy(current_board)
                new_board[possible_turns[0]] = self.markers[player]
                node.left = Node(new_board)

                recurse(node.left, "Player 1" if player == "Player 2" else "Player 2")
            else:
                shuffle(possible_turns)

                new_board1 = deepcopy(current_board)
                new_board2 = deepcopy(current_board)

                new_board1[possible_turns[0]] = self.markers[player]
                new_board2[possible_turns[1]] = self.markers[player]

                node.left = Node(new_board1)
                node.right = Node(new_board2)

                recurse(node.left, "Player 1" if player == "Player 2" else "Player 2")
                recurse(node.right, "Player 1" if player == "Player 2" else "Player 2")

        recurse(self._root, self.player)

    def point_counter(self):
        """
        Recursively counts points for the subtree.
        """
        def recurse(node):
            if node.left is not None:
                node.points += recurse(node.left)
            if node.right is not None:
                node.points += recurse(node.right)

            if node.left is None and node.right is None:
                match_result = node.board.calculate_result()
                if match_result == 1:
                    if self.player == "Player 1":
                        node.points = 1
                    if self.player == "Player 2":
                        node.points = -1
                elif match_result == -1:
                    if self.player == "Player 1":
                        node.points = -1
                    if self.player == "Player 2":
                        node.points = 1
                else:
                    node.points = 0

            return node.points

        recurse(self._root)

    def best_move(self):
        """
        Returns the best possible move starting from the root
        """
        if (self._root.left is None) or (self._root.right.points >= self._root.left.points):
            return self._root.right.board.last_turn[1]
        return self._root.left.board.last_turn[1]
