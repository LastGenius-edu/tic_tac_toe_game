#!/usr/bin/env python3
"""
Sultanov Andriy
MIT License 2020
"""
from btree import BinaryTree
from board import TicTacToeBoard


def test():
    board = TicTacToeBoard()
    tree = BinaryTree(board)
    tree.create_tree()
    print(tree._root.left)
    print(tree._root.right)


if __name__ == '__main__':
    test()
