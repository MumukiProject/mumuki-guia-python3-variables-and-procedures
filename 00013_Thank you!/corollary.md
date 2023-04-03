You may be wondering why we don't just leave the procedure empty. The problem with this is that we can't define an empty procedure in Python...

```python
def pass():
```

...nor have a single-comment body...

```python
def pass():
   # Passed
```

...since comments are ignored. However, `pass` works since it is the code representation of "do nothing". :exploding_head: