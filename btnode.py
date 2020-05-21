#!/usr/bin/env python3
"""
Sultanov Andriy
MIT License 2020
"""


class Node(object):
    """
    A Node class for the binary tree
    """

    def __init__(self, board, left=None, right=None):
        self.board = board
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.board)
