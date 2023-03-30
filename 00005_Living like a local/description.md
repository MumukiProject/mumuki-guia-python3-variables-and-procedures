Sometimes we don't want, or it just doesn't make sense, for every function to access our variables. Luckily, we can initialize variables both directly in the program and within a `def`:

```python
def longest_without_spaces(a_string, another_string):
  a_string_without_spaces = str.strip(a_string)
  another_string_without_spaces = str.strip(another_string)
 
  if len(a_string_without_spaces) > len(another_string_without_spaces):
	  return a_string_without_spaces
  else:
	  return another_string_without_spaces
```

Variables initialized within a `def`, known as _local variables_, are pretty straightforward, since they work exactly as we learned. However, you have to be extra careful :warning: since they can only be used within that definition. If you want to reference them in another place...

```python
question = "" + a_string_without_spaces + "?"
```

...boom! A `NameError` will be thrown! :collision:

However, variables initialized directly in the program, called _global variables_, can be read from any `def`. For example:

```python
maximum_weight_of_baggage_in_grams = 5000

def can_carry(luggage_weight):
  return luggage_weight <= maximum_weight_of_baggage_in_grams
````
 
> :telephone_receiver: :musical_keyboard: _Hello, it's me, I was wondering if all after these variables you'd like to greet..._
>
> Modify the `greet_to` function to avoid repeating logic. Use a local variable `end_of_greeting` in order to accomplish that.
