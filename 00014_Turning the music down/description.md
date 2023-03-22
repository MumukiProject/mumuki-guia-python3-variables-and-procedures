Let's take a look at the following program:

```python
volume = 40

def turn_volume_up(decibels):
  global volume
  volume += decibels

def turn_volume_down(decibels):
  global volume
  volume -= decibels

def is_safe_volume():
  return volume <= 75
```

> Check the correct statements: