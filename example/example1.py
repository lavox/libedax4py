'''
Example1
'''

from libedax4py import *

def printBoard(edax):
    # current board & player
    board = Board();
    edax.edax_get_board(board);
    currentPlayer = edax.edax_get_current_player();

    playerStone = "X" if (currentPlayer == libedax.BLACK) else "O";
    opponentStone = "O" if (currentPlayer == libedax.BLACK) else "X";

    print("  a b c d e f g h");
    for i in range(8):
        print(str(i + 1) + " ", end="");
        for j in range(8):
            if ((board.player & (1 << (j + 8 * i))) != 0):
                print(playerStone, end="");
            elif ((board.opponent & (1 << (j + 8 * i))) != 0):
                print(opponentStone, end="");
            else:
                print(".", end="");
            print(" ", end="");
        print("");
    print("");

def printHint(hint):
    print(" {0}: score = {1}".format(edaxutil.moveToString(hint.move), hint.score), end="");
    if (hint.book_move):
        print(", book", end="");
    else:
        print("({0},{1}), ".format(hint.lower, hint.upper), end="");
        print("{0}@{1}%, ".format(hint.depth, Hint.SELECTIVITY_TABLE[hint.selectivity]), end="");
        print("{0}ms, {1}nodes, ".format(hint.time, hint.n_nodes), end="");
        print("pv=", end="");
        for i in range(hint.pv[0].n_moves):
            print(edaxutil.moveToString(hint.pv[0].move[i]), end="");
    print("");

def printMoveString(edax):
    print("moves = {0}".format(edax.edax_get_moves(edaxutil.create_buffer(80 * 2 + 1)).decode()));

# obtain Edax object
edax = libedax.INSTANCE;

# initialize parameter. The first(0-th) value is ignored.
arg = ["", "-book-file", "../data/book.dat", "-eval-file", "../data/eval.dat", "-level", "17" ];

# initialize edax
edax.libedax_initialize(len(arg), edaxutil.to_cstr_array(arg));

# init command
edax.edax_init();

# play command
edax.edax_play(b"f5d6c3d3c4f4f6");

printBoard(edax);

# current discs & mobility
print("BLACK: {0}disc {1}moves ".format(edax.edax_get_disc(libedax.BLACK),
                                       edax.edax_get_mobility_count(libedax.BLACK)), end="");
print("WHITE: {0}disc {1}moves".format(edax.edax_get_disc(libedax.WHITE),
                                       edax.edax_get_mobility_count(libedax.WHITE)));

# hint command
hintlist = HintList();
edax.edax_hint(10, hintlist);
print("Hint result;");
for i in range(hintlist.n_hints):
    printHint(hintlist.hint[i + 1]);
print("");

# set level
edax.edax_set_option(b"-level", b"18");

# You can also obtain hint one by one.
print("Hint result (one by one) ;");
edax.edax_hint_prepare();
hint = Hint();
while True:
    #hint.clear(); // clear object when reusing object.
    edax.edax_hint_next(hint);
    if (hint.move != libedax.NOMOVE) :
        printHint(hint);
    else:
        break;
print("");

# check if current player can move
print("can move = " + str(edax.edax_can_move()));

# check if the game is over
print("is game over = " + str(edax.edax_is_game_over()));

# print moves
printMoveString(edax);
print();

# undo
edax.edax_undo();
print("Undo!");
printBoard(edax);

printMoveString(edax);
print();

# move c5
edax.edax_move(b"c5");
print("Move c5!");
printBoard(edax);

printMoveString(edax);
print();

# go command
edax.edax_go();
move = Move();
edax.edax_get_last_move(move);
print("Edax plays " + edaxutil.moveToString(move.x));
printBoard(edax);

printMoveString(edax);
print();

# set level
edax.edax_set_option(b"-level", b"7");

# mode command
print("mode changes to 1");
edax.edax_mode(1);
edax.edax_get_last_move(move);
print("Edax plays " + edaxutil.moveToString(move.x));
printBoard(edax);

printMoveString(edax);
print();

# mode command
print("mode changes to 2");
edax.edax_mode(2); # edax_mode runs until game is over
printBoard(edax);

printMoveString(edax);
print();

edax.libedax_terminate();
