Now that we know about procedures we can represent toggling scenarios using `not`. For example, turning a light on and off :bulb::

```python
light_on = False

def press_switch():
  global light_on
  light_on = not light_on
```

Now it's your turn!

> Define a `use_zip` procedure so that we can open and close our backpack. :school_satchel: