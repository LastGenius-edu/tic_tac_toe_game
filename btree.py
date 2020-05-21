#!/usr/bin/env python3
"""
Sultanov Andriy
MIT License 2020
"""
from btnode import Node


class BinaryTree:
    """
    BinaryTree for the TicTacToe game, representing a set
    of possible turns and consequent game boards
    """

    def __init__(self, starting_board, player):
        self._root = Node(starting_board)
        self.player = player

    def create_tree(self):
        """
        Builds a binary tree of possible boards.
        Chooses two turns randomly
        """
        def recurse(node, player):
            current_board = node.board

