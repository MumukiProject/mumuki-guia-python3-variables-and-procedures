
  def test_refill_500_in_thermos_with_200_increases_in_500_water_in_thermos_and_it_becomes_700(self):
    global water_in_thermos
    water_in_thermos = 200
    refill_thermos(500)
    self.assertEqual(water_in_thermos, 700)

  def test_refill_500_in_thermos_with_100_increases_in_500_water_in_thermos_and_it_becomes_600(self):
    global water_in_thermos
    water_in_thermos = 100
    refill_thermos(500)
    self.assertEqual(water_in_thermos, 600)

  def test_refill_300_in_thermos_with_250_increases_in_250_water_in_thermos_and_it_becomes_550(self):
    global water_in_thermos
    water_in_thermos = 300
    refill_thermos(250)
    self.assertEqual(water_in_thermos, 550)