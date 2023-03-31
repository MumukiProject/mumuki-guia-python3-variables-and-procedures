Did you notice something unusual in the "function" from the previous exercise :mag:? Let's look at it again:

```python
def spend_a_normal_day():
  global days_without_incidents_with_velociraptors
  days_without_incidents_with_velociraptors = days_without_incidents_with_velociraptors + 1
```

It doesn't have a `return`! But don't all functions require a `return`? :face_with_monocle:

That's right, and that means that `spend_a_normal_day()` isn't a true function - it's a _procedure_! :open_mouth: Although both functions and procedures are defined in the same way and both help us to simplify our tasks, they have some differences:

* functions **have no effect and return a value**, that is, they don't change our variables;
* procedures **do have an effect and return nothing** when called. Or - to be even more precise - procedures return `None`, which is the value that represents the absence of value 😵. 

> Now that you know the difference, define an `increase_fortune` procedure that doubles the value of the global variable `dollars_in_my_pocket`. Don't initialize that variable - we already did it for you, with a secret amount of money :wink:.
