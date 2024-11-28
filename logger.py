from rich import print as rprint
from functools import partial 


Verbose = True

Print = True
Write = False


def log(*args, **kwargs):
  msg = ' '.join(str(arg) for arg in args)
  rprint(msg)

