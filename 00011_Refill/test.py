
  def test_refill_500_ml_in_thermos_with_200_ml_increases_in_500_ml_water_in_thermos_and_it_becomes_700_ml(self):
    global water_in_thermos
    water_in_thermos = 200
    refill_thermos(500)
    self.assertEqual(water_in_thermos, 700)

  def test_refill_500_ml_in_thermos_with_100_ml_increases_in_500_ml_water_in_thermos_and_it_becomes_600_ml(self):
    global water_in_thermos
    water_in_thermos = 100
    refill_thermos(500)
    self.assertEqual(water_in_thermos, 600)

  def test_refill_300_ml_in_thermos_with_250_ml_increases_in_250_ml_water_in_thermos_and_it_becomes_550_ml(self):
    global water_in_thermos
    water_in_thermos = 300
    refill_thermos(250)
    self.assertEqual(water_in_thermos, 550)