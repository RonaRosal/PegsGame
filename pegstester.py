import importlib
import importlib.util
import sys
import traceback
import pprint

if len(sys.argv) != 2:
   print('''
Error: you must provide a filename for your pegs solution.

Make sure that this file is located in the same directory as your solution, along with 
graphs.py and digraphs.py if you use them.  Open a terminal, navigate to the directory
containing this file, and run

python pegstester.py pegs.py

replace pegs.py with the name of your solution file if it is different.
''')
   sys.exit(1)

try:
   filename = sys.argv[1]
   spec = importlib.util.spec_from_file_location('pegssolution', filename)
   if spec is None:
      print('''Error when loading the solution file.  There may be syntax errors, the file might not be valid Python code, or the file might not exist.''')
      sys.exit(1)
   pegssolution = importlib.util.module_from_spec(spec)
   spec.loader.exec_module(pegssolution)
except Exception:
   print("Problem parsing the solution file:")
   traceback.print_exc()
   sys.exit(1)

boards = {
   'XoXX': [(3, 'L'), (0, 'R')],
   'ooXoo': [],
   'XXoo': [(0, 'R')],
   'XXoXoXoXo': 'There are multiple solutions.  Check your solution manually',
   'XXXoXXXoXX': 'There are multiple solutions.  Check your solution manually',
   'XoooX': None,
   'ooXXXoXoXX': None
}

if 'pegsSolution' in dir(pegssolution):
   for board, realSolution in boards.items():
      solution = pegssolution.pegsSolution(board)
      print(f"Game board is {board}")
      print("Solution found: ", end='')
      pprint.pprint(solution)
      if type(solution) != list and solution is not None:
         print("Your solution is not a list or None.  Your return value is likely not correct.")
      print("Real solution:  ", end='')
      pprint.pprint(realSolution)
      print('-----------------------------------------------------------')
      

   print('''If the your solution is correct for the first board, but not for subsequent
boards then you may have variables that are only initialised once, and not for each time 
each your function is run.  This is likely to be a problem if you use global variables.
   ''')

   # We suggest that you create a method to automatically check if a solution is correct.
   # To do this, one method is to apply all moves in the solution to the starting game board 
   # and test if the result is a solved configuration.  Much of the code to do this
   # is required to find the solution anyway.
   # Note that the solution may not be unique!
else:
   print("Couldn't find pegsSolution() function!  Are you sure you provided the correct filename?")