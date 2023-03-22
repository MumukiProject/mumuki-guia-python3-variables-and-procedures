  
  def test_empty_thermos_assigns_0_to_water_in_thermos_if_it_was_500(self):
    global water_in_thermos
    water_in_thermos = 500
    empty_thermos()
    self.assertEqual(water_in_thermos, 0)

  def test_empty_thermos_assigns_0_to_water_in_thermos_if_it_was_200(self):
    global water_in_thermos
    water_in_thermos = 200
    empty_thermos()
    self.assertEqual(water_in_thermos, 0)

  def test_empty_thermos_assigns_0_to_water_in_thermos_if_it_was_1000(self):
    global water_in_thermos
    water_in_thermos = 1000
    empty_thermos()
    self.assertEqual(water_in_thermos, 0)

  def test_empty_thermos_leaves_in_0_the_water_in_thermos_if_it_was_in_0(self):
    global water_in_thermos
    water_in_thermos = 0
    empty_thermos()
    self.assertEqual(water_in_thermos, 0)

  def test_fill_thermos_assigns_1000_to_water_in_thermos_if_it_was_initially_80(self):
    global water_in_thermos
    water_in_thermos = 80
    fill_thermos()
    self.assertEqual(water_in_thermos, 1000)

  def test_fill_thermos_assigns_1000_to_water_in_thermos_if_it_was_initially_180(self):
    global water_in_thermos
    water_in_thermos = 180
    fill_thermos()
    self.assertEqual(water_in_thermos, 1000)

  def test_fill_thermos_assigns_1000_to_water_in_thermos_if_it_was_initially_840(self):
    global water_in_thermos
    water_in_thermos = 840
    fill_thermos()
    self.assertEqual(water_in_thermos, 1000)