  
  def test_elevator_is_not_overloaded_with_4_people_when_average_person_weight_in_kilograms_is_70(self):
    global average_person_weight_in_kilograms
    average_person_weight_in_kilograms = 70
    self.assertFalse(elevator_overloaded(4))

  def test_elevator_is_overloaded_with_4_people_when_average_person_weight_in_kilograms_is_80(self):
    global average_person_weight_in_kilograms
    average_person_weight_in_kilograms = 80
    self.assertTrue(elevator_overloaded(4))

  def test_elevator_is_not_overloaded_with_2_people_when_average_person_weight_in_kilograms_is_80(self):
    global average_person_weight_in_kilograms
    average_person_weight_in_kilograms = 80
    self.assertFalse(elevator_overloaded(2))

  def test_elevator_is_overloaded_with_5_people_when_average_person_weight_in_kilograms_is_80(self):
    global average_person_weight_in_kilograms
    average_person_weight_in_kilograms = 80
    self.assertTrue(elevator_overloaded(5))