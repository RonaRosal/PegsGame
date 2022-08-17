# PegsGame
Returns a sequence of jumps that results in a board with a single peg. 


-- GAME DESCRIPTION --

The puzzle board is a line of regularly spaced holes. The number of holes can vary. The puzzle starts with
some of the holes occupied by pegs, and some holes empty. The player proceeds by a series of jumps. In a
jump, a peg moves over an adjacent peg into an empty hole. The peg which was jumped over is removed.
The goal of the puzzle is to find a sequence of jumps so that the board ends up with a single peg and all
other holes empty.
For this project, the game board’s starting position is given as a Python string like so:

XoXoooXXoo

where X indicates a peg and o indicates an empty hole. An example of a valid jump would take this:

XooXX
to this:

XoXoo

where the rightmost peg has jumped to the left, removing the second from last peg.
Your goal is to write a Python function pegsSolution(gameBoard) which returns a sequence of jumps that
results in a board with a single peg. The sequence of jumps should be a Python list like so:
[ (3, ’L’), (5, ’R’), (4, ’L’) ]
where each item in the list is a pair indicating the position of the peg which is jumping (counting from 0
on the left of the board) and the direction (either L or R for left or right). If there is no sequence of jumps
which wins the game, then your function should return None.

Promises:

• The input string will consist of a single line of the characters X and o only.

• The input string will be at least three characters long.
