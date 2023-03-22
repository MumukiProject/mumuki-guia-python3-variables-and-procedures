
  def test_greet_to_Umi_at_11_returns_good_morning(self):
    self.assertEquals(greet_to("Umi", 11), "Good morning Umi!")
    
  def test_greet_to_May_at_12_returns_good_afternoon(self):
    self.assertEquals(greet_to("May", 12), "Good afternoon May!")
    
  def test_greet_to_Lu_at_18_returns_good_afternoon(self):
    self.assertEquals(greet_to("Lu", 18), "Good afternoon Lu!")
    
  def test_greet_to_Dani_at_19_returns_good_evening(self):
    self.assertEquals(greet_to("Dani", 19), "Good evening Dani!")
  
  def test_greet_to_Feli_at_20_returns_good_evening(self):
    self.assertEquals(greet_to("Feli", 20), "Good evening Feli!")