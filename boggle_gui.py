# Python's most basic GUI. 
# To install: sudo apt-get install python3-tk
from tkinter import *

# All of boggle-solving code is in the file boggle_solver.py
import boggle_solver

# used for randomly filling a boggle board
import random

# A conventional boggle grid is 4 x 4
SIZE = 4
# A letter bank for "randomly" selecting letters. More useful 
# letters have a higher probability of being selected.
alphabet = \
	"AAAAAABBCCDDDEEEEEEEEEEEFFGGHHHHHIIIIIIJKLLLLMM"+\
	"NNNNNNOOOOOOOPPQRRRRRSSSSSSTTTTTTTTTUUUVVWWWXYYYZ"



# The class for handling the text box that displays 
# the valid words on the boggle board
class Display(Frame):

	def __init__(self, root):

		Frame.__init__(self, root)

		# enables us to use the grid layout manager
		self.grid()

		# makes the text box and places it 
		self.display_text = \
			Text(right_side, height = 10, width = SIZE*SIZE, \
				font = ("courier new", 16))
		self.display_text.grid(row=0, column=0)

		# initialize the list of words that will be displayed
		# in the text box
		self.word_list = []


	# Takes in a set of words to be displayed in the text field
	# and displays them in descending order of length
	def display_words(self, set_of_words):

		# first we clear to text field so that these new words
		# replace any previous words
		self.clear()

		# the valid words will be passed in as a set, so we need
		# to convert them into a list
		words = list(set_of_words)

		# first, we sort this list alphabetically
		words.sort()

		# next we sort the list in reverse order of word length,
		# so that the most impressive (read: long) words are 
		# displayed first
		words.sort(key=lambda x:len(x), reverse=True)

		# We set the display's word list equal to this correctly
		# sorted list
		self.word_list = words

		# Finally, we display all of the words in the text box
		for word in words:
			self.display_text.insert(END, word+'\n')


	# Clears the text box by deleting all its contents
	def clear(self):
		self.display_text.delete("0.0", END)


	# Responds to the sort by length button. 
	def sort_by_len(self):

		# We start by clearing the text box of words
		self.clear()

	# The stored word list is already sorted by length, 
	# so we simply display each word
		for word in self.word_list:
			self.display_text.insert(END, word+'\n')


	# Sorts the current list of valid words on the board and 
	# displays them alphabetically
	def alpha_sort(self):

		# first clear the display
		self.clear()

		# sort the word list alphabetically
		words = sorted(self.word_list)

		# display each word int the text box
		for word in words:
			self.display_text.insert(END, word+'\n')



# The class for handling the grid of text entry boxes that 
# takes in the letters on the boggle board from the user
class Board(Frame):

	def __init__(self, root, display):
		Frame.__init__(self, root)

		# Uses the grid layout manager
		self.grid()

		# Makes a SIZE x SIZE grid of text entry boxes
		self.entries = []
		for i in range(SIZE):
			self.entries.append([])
			for j in range(SIZE):
				contents = StringVar()
				e = Entry(text=contents, font = ("courier new", 36), width=1)
				e.grid(row = i, column = j, padx = 16)
				self.entries[-1].append(e)


	# Clears the input boggle board
	def clear(self):

		# Delete each item on the grid
		for listy in self.entries:
			for entry in listy:
				entry.delete(0, END)

		# Clear the valid words text box as well
		display.clear()

		# Indicate that the list of valid words is now empty
		display.word_list = []


	# Populates the boggle board with random letters
	def random_board(self):

		# For every call on the board, delete what's currently
		# there and replace it with a randomly chosen letter
		for listy in self.entries:
			for entry in listy:
				entry.delete(0, END)
				entry.insert(0, random.choice(alphabet))

		# clear the text field, since it contains the words associated
		# with the now past board rather than the current board
		display.clear()


	# Finds all of the valid words on the boggle board and displays them
	def find_words(self):

		# Make a two-dimensional array that represents the letters
		# on the boggle board
		array_of_letters = []
		for listy in self.entries:
			col = []
			for entry in listy:
				letter = entry.get()

				# Make sure that each text box contains only one letter. If 
				# not, the board is invalid, so we display an error message
				# and return.
				if len(letter) > 1:
					display.display_words\
						(["some entries\ncontain more\nthan one\ncharacter"])
					return

				col.append(entry.get())
			array_of_letters.append(col)

		# Now that we have all our letters, we 
		display.display_words(boggle_solver.solve_boggle(array_of_letters))



# A class for handling the buttons 
class Controls(Frame):

	def __init__(self, root, board, display):
		Frame.__init__(self, root)
		# use the grid layout manager to arrange the buttons
		self.grid()

		# Makes the "find words" button, which finds all the valid words
		start_button = \
			Button(self, text="find words", command=board.find_words)
		
		# Makes the "clear" button, which clears both the board and the
		# valid words text box
		clear_button = Button(self, text = "clear", command=board.clear)
		
		# Makes the "random" button, which populates the boggle board with
		# random letters
		random_button = \
			Button(self, text="random", command=board.random_board)
		
		# Makes the "sort by length" button, which displays the valid boggle
		# words in the text box in descending order of length
		sort_len_button = \
			Button(self, text="sort by length", command=display.sort_by_len)

		# Makes the "sort alphabetically" button, which displays the valid 
		# boggle words in the text box in alphabetical order
		sort_alpha_button = Button\
			(self, text="sort alphabetically", command=display.alpha_sort)

		# Place all the buttons on the grid layout
		start_button.grid(row = 0, column = 2)
		clear_button.grid(row = 0, column = 1)
		random_button.grid(row = 0, column = 0)
		sort_len_button.grid(row = 0, column = 4)
		sort_alpha_button.grid(row = 0, column = 3)



if __name__ == '__main__':


	# Makes an instance of the Tkinter GUI and gives it a title
	root = Tk()
	root.title("Boggle Solver")

	# Creates and places the areas on the grid layout
	upper_left = Frame(root)
	upper_left.grid(row = 0)
	lower_left = Frame(root)
	lower_left.grid(row = SIZE, columnspan = SIZE*2)
	right_side = Frame(root)
	right_side.grid(row = 0, rowspan = SIZE, column = SIZE)

	# Puts instances of the boggle board frame, the button frame, 
	# and the display text box frame in the areas on the grid layout
	display = Display(right_side)
	board = Board(upper_left, display)
	controls = Controls(lower_left, board, display)

	# Starts the GUI
	root.mainloop()