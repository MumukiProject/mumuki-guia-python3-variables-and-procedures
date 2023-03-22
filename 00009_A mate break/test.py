  
  def test_water_in_thermos_is_initially_at_1000(self):
    self.assertEqual(water_in_thermos, 1000, "water_in_thermos must be initialized with 1000")

  def test_pour_water_decreases_30_ml_water_in_thermos(self):
    global water_in_thermos
    water_in_thermos = 1000
    pour_water()
    self.assertEqual(water_in_thermos, 970)

  def test_pouring_3_mates_decreases_90_ml_water_in_thermos(self):
    global water_in_thermos
    water_in_thermos = 1000
    pour_water()
    pour_water()
    pour_water()
    self.assertEqual(water_in_thermos, 910)
    