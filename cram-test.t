Check out khmer-ngram::

  $ git clone git://github.com/ctb/khmer-ngram.git
  Initialized empty Git repository in .* (re)
  $ cd khmer-ngram
  $ ls
  README.txt
  basic.html
  basic.txt
  cram-test.t
  data
  graphsize-book.py
  hash.py
  load-book.py
  run-doctests.py
  shred-book.py

...and run the doctests::

  $ python run-doctests.py basic.txt
  ... running doctests on basic.txt
  *** SUCCESS ***

Add in another block of text for grins::

  $ ls
  README.txt
  basic.html
  basic.txt
  cram-test.t
  data
  graphsize-book.py
  hash.py
  hash.pyc
  load-book.py
  run-doctests.py
  shred-book.py

Can I make this a doctest, by including Python code?

 >>> print 'why, yes I can!'
 why, yes I can!

Awesome.
