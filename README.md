# boggle-solver-using-trie

HOW TO USE

Run the boggle solver with:

	> python3 boggle_gui.py

The program uses Tkinter, Python's standard GUI package. If you don't 
already have Tkinter, you can install it with:

	> sudo apt-get install python3-tk

If you're disinterested in the GUI, you could just go directly to 
boggle_solver.py and run solve_boggle() on a two-dimensional list 
representing your boggle board. An example is included at the bottom
of that file.

ABOUT

This program demonstrates how a trie tree can provide an efficient means 
for solving word-finding problems such as boggle. To search a board for valid
words, we conduct depth-first searches originating from each location on the 
board. In these searches, we follow each path on the board alongside its 
corresponding path down the trie. Whenever we reach a trie node that indicates 
the end of a word, we add that to our set of valid words on the board. As we 
traverse the board, we stop whenever the trie reaches a dead-end, indicating 
that there are no possible words along our current path on the board. This is
a huge time saver because we don't need to check every possible combination of
consecutive letters on the board, since the trie will only guide us down 
plausible paths.  

CONTENTS

boggle_gui.py - contains the GUI for the boggle solver

boggle_solver.py - contains the algorithm for finding all the words on a
boggle board

my_trie.py - contains the code for the trie tree data structure

words.txt - a dictionary, used for finding valid words

DISCLAIMER

This program is not affiliated with Hasbro, Inc., the manufacturer of 
Boggle, and is intended for educational purposes only. 
