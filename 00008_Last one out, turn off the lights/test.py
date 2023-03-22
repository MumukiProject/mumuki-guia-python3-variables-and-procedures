  
  def test_if_backpack_is_open_when_invoking_use_zip_it_becomes_closed(self):
    use_zip()
    self.assertFalse(backpack_open)
  
  def test_if_backpack_is_closed_when_invoking_use_zip_it_becomes_open(self):
    global backpack_open
    backpack_open = False
    use_zip()
    self.assertTrue(backpack_open)
  
  def test_if_backpack_is_open_when_invoking_use_zip_two_times_it_remains_open(self):
    use_zip()
    use_zip()
    self.assertTrue(backpack_open)