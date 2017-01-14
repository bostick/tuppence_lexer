from setuptools import setup, find_packages
 
setup (
  name='tuppence_lexer',
  packages=find_packages(),
  entry_points =
  """
  [pygments.lexers]
  tuppence_lexer = tuppence_lexer.tuppence_lexer:TuppenceLexer
  """,
)
