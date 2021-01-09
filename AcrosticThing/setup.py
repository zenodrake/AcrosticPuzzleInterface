#!/usr/bin/env python3

from distutils.core import setup
# from cx_Freeze import setup, Executable
import sys


setup(
    name='AcrosticPuzzleHelper',
    version='0.1',
    description='A very simple tool to help solve acrostic crossword puzzles',
    author='Andrew Keeler',
    py_modules=['AcrosticPuzzle', 'AnswerCellDisplay', 'ClueDisplay', 'ClueFrame', 'EnterNewPuzzleWindow', 'GridEntry', 'PuzzleFrame'],
    entry_points={'console_scripts': ['acrostic = AcrosticPuzzle:main']}
)
