  
  def test_perimeter_of_a_circle_of_radius_1_is_correct(self):
    self.assertEqual(perimeter_circle(1), 6.28318530717958)
  
  def test_perimeter_of_a_circle_of_radius_2_is_correct(self):
    self.assertEqual(perimeter_circle(2), 12.56637061435916)
  
  def test_perimeter_of_a_circle_of_radius_0_is_correct(self):
    self.assertEqual(perimeter_circle(0), 0)
  
  def test_area_of_a_circle_of_radius_1_is_correct(self):
    self.assertEqual(area_circle(1), 3.14159265358979)
  
  def test_area_of_a_circle_of_radius_2_is_correct(self):
    self.assertEqual(area_circle(2), 12.56637061435916)
  
  def test_area_of_a_circle_of_radius_0_is_correct(self):
    self.assertEqual(area_circle(0), 0)
