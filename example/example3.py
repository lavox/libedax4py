'''
Example3
'''

from libedax4py import *

# obtain Edax object
edax = libedax.INSTANCE;

# you can use board.c/bit.c functions without initialize libedax
p = 0x0000000810000000;
o = 0x0000001008000000;

print("can_move = {0}".format(edax.can_move(p, o)));
print("get_moves = {0}".format(hex(edax.get_moves(p, o))));

print("first_bit = {0}".format(edax.first_bit(p)));
print("last_bit = {0}".format(edax.last_bit(p)));
