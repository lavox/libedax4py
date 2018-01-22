'''
Example2
'''

from libedax4py import *

# obtain Edax object
edax = libedax.INSTANCE;

# initialize parameter. The first(0-th) value is ignored.
arg = ["", "-book-file", "../data/book.dat", "-eval-file", "../data/eval.dat", "-level", "17" ];

# initialize edax
edax.libedax_initialize(len(arg), edaxutil.to_cstr_array(arg));

# init command
edax.edax_init();

# book new command
print("book new 15 30 command.");
edax.edax_book_new(15, 30);

# set book-file option
print("set -book-file ../data/book_example.dat command.");
edax.edax_set_option(b"-book-file", b"../data/book_example.dat");

# play command
print("play f5d6c5f4e3c6d3f6e6d7 command.");
edax.edax_play(b"f5d6c5f4e3c6d3f6e6d7");

# book store command
print("book store command.");
edax.edax_book_store();

# init command
print("init command.");
edax.edax_init();

# play command
print("play f5d6c3d3 command.");
edax.edax_play(b"f5d6c3d3");

# book store command
print("book store command.");
edax.edax_book_store();

# book save command
print("book save ../data/book_example.dat command.");
edax.edax_book_save(b"../data/book_example.dat");

# init command
print("init command.");
edax.edax_init();

# play command
print("play f5d6 command.");
edax.edax_play(b"f5d6");
print();

# book show command
position = Position();
edax.edax_book_show(position);

print("Position information:");
print(" score : {0} ({1},{2})".format(position.score.value,
                                      position.score.lower, position.score.upper));
print(" link  : ", end="");
link = position.link;
for i in range(position.n_link):
    print("{0}={1}, ".format(edaxutil.moveToString(link[i].move), link[i].score), end="");
print("");
print(" leaf  : {0}={1}".format(edaxutil.moveToString(position.leaf.move), position.leaf.score));
print(" wins  : {0}".format(position.n_wins));
print(" draws : {0}".format(position.n_draws));
print(" losses: {0}".format(position.n_losses));
print(" lines : {0}".format(position.n_lines));
print(" level : {0}".format(position.level));
print();

# book info command
book = Book();
edax.edax_book_info(book);
print("Book information:");
print(" date   : {0}/{1}/{2} {3}:{4}:{5}".format(book.date.year, 
                 book.date.month, book.date.day, book.date.hour,
                 book.date.minute, book.date.second));
print(" options:");
print("   level : {0}".format(book.options.level));
print("   depth : {0}".format(61 - book.options.n_empties));
print("   error : midgame={0}, endcut={1}".format(book.options.midgame_error,
                                                  book.options.endcut_error));
print(" nodes : {0}".format(book.n_nodes));

edax.libedax_terminate();
