# tuppence_lexer
A Pygments lexer for Tuppence



http://pygments.org/docs/plugins/#entrypoints

```
cd tuppence_lexer

python3 setup.py develop

pygmentize -f html -O full ~/Documents/GitHub/tuppence/examples/sqrt.2p > /tmp/sqrt.html
```


Using the Jupyter console interface seems to give  
`/Library/Frameworks/Python.framework/Versions/3.5/lib/python3.5/site-packages/jupyter_console/ptshell.py:94: UserWarning: No lexer found for language 'tuppence'. Treating as plain text.`, but using the Jupyter notebook interface works.


