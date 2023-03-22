_But why are they called variables if they don't vary?_ :face_with_raised_eyebrow:

Well, it's just that they can actually vary :sunglasses: . Let's see a prehistoric example 🦖:

```python
# initialize the variable to be 0...
days_without_incidents_with_velociraptors = 0

# ...and later, we update it
days_without_incidents_with_velociraptors = days_without_incidents_with_velociraptors + 1

# now is equal to 1!
days_without_incidents_with_velociraptors
```

However, we must be especially careful when working with global variables: if we want to modify them inside a function, we declare it as `global`:

```python
# initialize the variable at the beginning of our program
days_without_incidents_with_velociraptors = 0

def spend_a_normal_day():
  # we tell Python that we are going to make modifications to the global variable
  global days_without_incidents_with_velociraptors

  # now we can update it
  days_without_incidents_with_velociraptors = days_without_incidents_with_velociraptors + 1
```

> Test the following statements in the console, in order:
>
> 1. `days_without_incidents_with_velociraptors`
> 2. `spend_a_normal_day()`
> 3. `spend_a_normal_day()`
> 4. `spend_a_normal_day()`
> 5. `days_without_incidents_with_velociraptors`

> You can use the arrow keys on your keyboard to navigate between commands that have already been executed. :arrow_up_small: :arrow_down_small:
