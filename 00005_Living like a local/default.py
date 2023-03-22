def greet_to(who, hour):
  if hour < 12:
    return "Good morning " + who + "!"
  elif hour < 19:
    return "Good afternoon " + who + "!"
  else: 
    return "Good evening " + who + "!"