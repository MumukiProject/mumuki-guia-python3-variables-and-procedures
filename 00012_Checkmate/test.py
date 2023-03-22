  
  def test_pour_water_decreases_30_ml_the_water_in_thermos(self):
    global water_in_thermos
    water_in_thermos = 1000
    pour_water()
    self.assertEqual(water_in_thermos, 970)

  def test_pour_water_3_times_decreases_90_ml_the_water_in_thermos(self):
    global water_in_thermos
    water_in_thermos = 1000
    pour_water()
    pour_water()
    pour_water()
    self.assertEqual(water_in_thermos, 910)
    
  def test_pour_water_increases_30_ml_the_water_in_mate(self):
    global water_in_mate
    water_in_mate = 0
    pour_water()
    self.assertEqual(water_in_mate, 30)
    
  def test_drink_mate_assigns_0_to_water_in_mate(self):
    global water_in_mate
    water_in_mate = 20
    drink_mate()
    self.assertEqual(water_in_mate, 0)