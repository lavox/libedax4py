'''
@author: lavox
'''

from ctypes import *
from ctypes.util import find_library
from sys import platform as _platform

module_name = ""
if _platform == "linux" or _platform == "linux2":
    module_name = "libedax.so";
elif _platform == "darwin":
    module_name = "libedax.dylib";
elif _platform == "win32":
    module_name = "libedax-x86.dll";
elif _platform == "win64":
    module_name = "libedax-x64.dll";

del _platform;

import os
print(find_library(module_name));
#INSTANCE = cdll.LoadLibrary(os.path.abspath(__file__ + "/../" + module_name));
INSTANCE = cdll.LoadLibrary(find_library(module_name));
del os;

BLACK = 0;
''' Black. '''
    
WHITE = 1;
''' White. '''

PASS = 64;
''' Pass. '''

NOMOVE = 65;
''' No Move. '''

class Board(Structure):
    """
    Board class.
    """
    
    _fields_ = [("player", c_ulonglong), ("opponent", c_ulonglong)];


class Date(Structure):
    """
    Date class.
    """
    
    _fields_ = [("year", c_short), ("month", c_byte), ("day", c_byte)
                , ("hour", c_byte), ("minute", c_byte), ("second", c_byte)];


class Options(Structure):
    """
    Options class.
    """
    
    _fields_ = [("level", c_int), ("n_empties", c_int), ("midgame_error", c_int)
                , ("endcut_error", c_int), ("verbosity", c_int)];


class Stats(Structure):
    """
    Stats class.
    """
    
    _fields_ = [("n_nodes", c_int), ("n_links", c_int), ("n_todo", c_int)];


class Random(Structure):
    """
    Random class.
    """
    
    _fields_ = [("x", c_ulonglong)];



class Book(Structure):
    """
    Book class.
    """
    
    _fields_ = [("date", Date), ("options", Options), ("stats", Stats),
                ("array", c_void_p), ("stack", c_void_p), ("n", c_int),
                ("n_nodes", c_int), ("need_saving", c_bool), ("random", Random),
                ("search", c_void_p)];


class Line(Structure):
    """
    Line class.
    """
    
    _fields_ = [("move", c_char * 80), ("n_moves", c_int), ("color", c_int)];


class Hint(Structure):
    """
    Hint class.
    """
    
    SELECTIVITY_TABLE = [73, 87, 95, 98, 99, 100];
    
    _fields_ = [("depth", c_int), ("selectivity", c_int), ("move", c_int),
                ("score", c_int), ("upper", c_int), ("lower", c_int),
                ("pv", Line * 1), ("time", c_longlong), ("n_nodes", c_ulonglong),
                ("book_move", c_bool)];


class HintList(Structure):
    """
    Hint List class.
    """
    
    _fields_ = [("hint", Hint * 34), ("n_hints", c_int)];


class Link(Structure):
    """
    Link class.
    """
    
    _fields_ = [("score", c_byte), ("move", c_ubyte)];


class Move(Structure):
    """
    Move class.
    """
    
    _fields_ = [("flipped", c_ulonglong), ("x", c_int), ("score", c_int),
                ("cost", c_uint), ("next", c_void_p)];


class MoveList(Structure):
    """
    Move List class.
    """
    
    _fields_ = [("move", Move * 34), ("n_moves", c_int)];


class Score(Structure):
    """
    Score class.
    """
    
    _fields_ = [("value", c_short), ("lower", c_short), ("upper", c_short)];


class Position(Structure):
    """
    Position class.
    """
    
    _fields_ = [("board", Board * 1), ("leaf", Link), ("link", POINTER(Link)),
                ("n_wins", c_uint), ("n_draws", c_uint), ("n_losses", c_uint),
                ("n_lines", c_uint), ("score", Score), ("n_link", c_ubyte),
                ("level", c_ubyte), ("done", c_ubyte), ("todo", c_ubyte)];


INSTANCE.libedax_initialize.restype = None;
INSTANCE.libedax_initialize.argtypes = [c_int, POINTER(c_char_p)];

INSTANCE.libedax_terminate.restype = None;
INSTANCE.libedax_terminate.argtypes = [];

INSTANCE.edax_init.restype = None;
INSTANCE.edax_init.argtypes = [];

INSTANCE.edax_new.restype = None;
INSTANCE.edax_new.argtypes = [];

INSTANCE.edax_load.restype = None;
INSTANCE.edax_load.argtypes = [c_char_p];

INSTANCE.edax_save.restype = None;
INSTANCE.edax_save.argtypes = [c_char_p];

INSTANCE.edax_undo.restype = None;
INSTANCE.edax_undo.argtypes = [];

INSTANCE.edax_redo.restype = None;
INSTANCE.edax_redo.argtypes = [];

INSTANCE.edax_mode.restype = None;
INSTANCE.edax_mode.argtypes = [c_int];

INSTANCE.edax_setboard.restype = None;
INSTANCE.edax_setboard.argtypes = [c_char_p];

INSTANCE.edax_setboard_from_obj.restype = None;
INSTANCE.edax_setboard_from_obj.argtypes = [POINTER(Board), c_int];

INSTANCE.edax_vmirror.restype = None;
INSTANCE.edax_vmirror.argtypes = [];

INSTANCE.edax_hmirror.restype = None;
INSTANCE.edax_hmirror.argtypes = [];

INSTANCE.edax_rotate.restype = None;
INSTANCE.edax_rotate.argtypes = [c_int];

INSTANCE.edax_symetry.restype = None;
INSTANCE.edax_symetry.argtypes = [c_int];

INSTANCE.edax_play.restype = None;
INSTANCE.edax_play.argtypes = [c_char_p];

INSTANCE.edax_force.restype = None;
INSTANCE.edax_force.argtypes = [c_char_p];

INSTANCE.edax_go.restype = None;
INSTANCE.edax_go.argtypes = [];

INSTANCE.edax_hint.restype = None;
INSTANCE.edax_hint.argtypes = [c_int, POINTER(HintList)];

INSTANCE.edax_hint_prepare.restype = None;
INSTANCE.edax_hint_prepare.argtypes = [];

INSTANCE.edax_hint_next.restype = None;
INSTANCE.edax_hint_next.argtypes = [POINTER(Hint)];

INSTANCE.edax_stop.restype = None;
INSTANCE.edax_stop.argtypes = [];

INSTANCE.edax_move.restype = c_bool;
INSTANCE.edax_move.argtypes = [c_char_p];

INSTANCE.edax_opening.restype = c_char_p;
INSTANCE.edax_opening.argtypes = [];

INSTANCE.edax_ouverture.restype = c_char_p;
INSTANCE.edax_ouverture.argtypes = [];

INSTANCE.edax_book_store.restype = None;
INSTANCE.edax_book_store.argtypes = [];

INSTANCE.edax_book_on.restype = None;
INSTANCE.edax_book_on.argtypes = [];

INSTANCE.edax_book_off.restype = None;
INSTANCE.edax_book_off.argtypes = [];

INSTANCE.edax_book_randomness.restype = None;
INSTANCE.edax_book_randomness.argtypes = [c_int];

INSTANCE.edax_book_depth.restype = None;
INSTANCE.edax_book_depth.argtypes = [c_int];

INSTANCE.edax_book_new.restype = None;
INSTANCE.edax_book_new.argtypes = [c_int, c_int];

INSTANCE.edax_book_load.restype = None;
INSTANCE.edax_book_load.argtypes = [c_char_p];

INSTANCE.edax_book_save.restype = None;
INSTANCE.edax_book_save.argtypes = [c_char_p];

INSTANCE.edax_book_import.restype = None;
INSTANCE.edax_book_import.argtypes = [c_char_p];

INSTANCE.edax_book_export.restype = None;
INSTANCE.edax_book_export.argtypes = [c_char_p];

INSTANCE.edax_book_merge.restype = None;
INSTANCE.edax_book_merge.argtypes = [c_char_p];

INSTANCE.edax_book_fix.restype = None;
INSTANCE.edax_book_fix.argtypes = [];

INSTANCE.edax_book_negamax.restype = None;
INSTANCE.edax_book_negamax.argtypes = [];

INSTANCE.edax_book_correct.restype = None;
INSTANCE.edax_book_correct.argtypes = [];

INSTANCE.edax_book_prune.restype = None;
INSTANCE.edax_book_prune.argtypes = [];

INSTANCE.edax_book_subtree.restype = None;
INSTANCE.edax_book_subtree.argtypes = [];

INSTANCE.edax_book_show.restype = None;
INSTANCE.edax_book_show.argtypes = [POINTER(Position)];

INSTANCE.edax_book_info.restype = None;
INSTANCE.edax_book_info.argtypes = [POINTER(Book)];

INSTANCE.edax_book_verbose.restype = None;
INSTANCE.edax_book_verbose.argtypes = [c_int];

INSTANCE.edax_book_add.restype = None;
INSTANCE.edax_book_add.argtypes = [c_char_p];

INSTANCE.edax_book_check.restype = None;
INSTANCE.edax_book_check.argtypes = [c_char_p];

INSTANCE.edax_book_extract.restype = None;
INSTANCE.edax_book_extract.argtypes = [c_char_p];

INSTANCE.edax_book_deviate.restype = None;
INSTANCE.edax_book_deviate.argtypes = [c_int, c_int];

INSTANCE.edax_book_enhance.restype = None;
INSTANCE.edax_book_enhance.argtypes = [c_int, c_int];

INSTANCE.edax_book_fill.restype = None;
INSTANCE.edax_book_fill.argtypes = [c_int];

INSTANCE.edax_book_play.restype = None;
INSTANCE.edax_book_play.argtypes = [];

INSTANCE.edax_book_deepen.restype = None;
INSTANCE.edax_book_deepen.argtypes = [];

INSTANCE.edax_book_feed_hash.restype = None;
INSTANCE.edax_book_feed_hash.argtypes = [];

INSTANCE.edax_base_problem.restype = None;
INSTANCE.edax_base_problem.argtypes = [c_char_p, c_int, c_char_p];

INSTANCE.edax_base_tofen.restype = None;
INSTANCE.edax_base_tofen.argtypes = [c_char_p, c_int, c_char_p];

INSTANCE.edax_base_correct.restype = None;
INSTANCE.edax_base_correct.argtypes = [c_char_p, c_int];

INSTANCE.edax_base_complete.restype = None;
INSTANCE.edax_base_complete.argtypes = [c_char_p];

INSTANCE.edax_base_convert.restype = None;
INSTANCE.edax_base_convert.argtypes = [c_char_p, c_char_p];

INSTANCE.edax_base_unique.restype = None;
INSTANCE.edax_base_unique.argtypes = [c_char_p, c_char_p];

INSTANCE.edax_set_option.restype = None;
INSTANCE.edax_set_option.argtypes = [c_char_p, c_char_p];

INSTANCE.edax_get_moves.restype = c_char_p;
INSTANCE.edax_get_moves.argtypes = [c_char_p];

INSTANCE.edax_is_game_over.restype = c_bool;
INSTANCE.edax_is_game_over.argtypes = [];

INSTANCE.edax_can_move.restype = c_bool;
INSTANCE.edax_can_move.argtypes = [];

INSTANCE.edax_get_last_move.restype = None;
INSTANCE.edax_get_last_move.argtypes = [POINTER(Move)];

INSTANCE.edax_get_board.restype = None;
INSTANCE.edax_get_board.argtypes = [POINTER(Board)];

INSTANCE.edax_get_current_player.restype = c_int;
INSTANCE.edax_get_current_player.argtypes = [];

INSTANCE.edax_get_disc.restype = c_int;
INSTANCE.edax_get_disc.argtypes = [c_int];

INSTANCE.edax_get_mobility_count.restype = c_int;
INSTANCE.edax_get_mobility_count.argtypes = [c_int];

### board.c function

INSTANCE.get_moves.restype = c_ulonglong;
INSTANCE.get_moves.argtypes = [c_ulonglong, c_ulonglong];

INSTANCE.can_move.restype = c_bool;
INSTANCE.can_move.argtypes = [c_ulonglong, c_ulonglong];

### bit.c function

INSTANCE.bit_count.restype = c_int;
INSTANCE.bit_count.argtypes = [c_ulonglong];

INSTANCE.first_bit.restype = c_int;
INSTANCE.first_bit.argtypes = [c_ulonglong];

INSTANCE.last_bit.restype = c_int;
INSTANCE.last_bit.argtypes = [c_ulonglong];

