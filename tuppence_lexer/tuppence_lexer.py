from pygments.lexer import RegexLexer, include, words
from pygments.token import Text, Comment, Operator, Keyword, Name, String, \
    Number, Punctuation, Error, Whitespace

__all__ = ['TuppenceLexer']


class TuppenceLexer(RegexLexer):
    name = 'Tuppence'
    aliases = ['tuppence']
    filenames = ['*.2p']
    mimetypes = ['application/x-tuppence']

    tokens = {
        'root': [
            (r'(;.*)', Comment.Single),

            (r'(\s)', Text),

            (r'(\d+)', Number.Integer),
            (r'(`(0|1)*`)', Number.Bin),

            (r'(=|\+|\-|\*|/|#|%%|>>|>%|\.\.\.)', Operator),

            (r'\bdefine|exit|for|print|rationalize|while\b', Keyword),
            
            (r'\b[_a-zA-Z][_a-zA-Z0-9]*\b', Name.Variable),

            (r'(\(|\))', Punctuation),
            (r'(\{|\})', Punctuation),

            (r'\,', Punctuation),
        ]
    }
