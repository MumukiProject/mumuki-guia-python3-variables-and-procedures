  
  def test_increase_fortune_duplicated_the_global_variable_dollars_in_my_pocket(self):
    global dollars_in_my_pocket
    dollars_in_my_pocket = 100
    increase_fortune()
    self.assertEqual(dollars_in_my_pocket, 200)


  def test_increase_fortune_can_be_invoked_several_times(self):
    global dollars_in_my_pocket
    dollars_in_my_pocket = 30
    increase_fortune()
    increase_fortune()
    increase_fortune()
    self.assertEqual(dollars_in_my_pocket, 240)