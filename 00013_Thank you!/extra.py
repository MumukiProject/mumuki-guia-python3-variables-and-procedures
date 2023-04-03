water_in_mate = 0
water_in_thermos = 1000

def pour_water():
  global water_in_mate
  global water_in_thermos
  water_in_thermos -= 30
  water_in_mate += 30
  
def drink_mate():
  global water_in_mate
  water_in_mate = 0
  
def i_pass():
  pass