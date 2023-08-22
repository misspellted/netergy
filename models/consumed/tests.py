

import unittest
from models.consumed.v0 import ConsumedEnergy as V0


class TestConsumedEnergyV0(unittest.TestCase):
  def test_validate_without_any_detials(self):
    self.assertFalse(V0.validate())

  def test_validate_with_empty_detials(self):
    details = dict()
    self.assertFalse(V0.validate(**details))

  def test_validate_without_all_detials(self):
    details = dict()
    details[V0.UTC_START_DATE[0]] = "2023-08-21"
    details[V0.UTC_START_TIME[0]] = "16:38"
    self.assertFalse(V0.validate(**details))

  def test_validate_with_all_detials(self):
    details = dict()
    details[V0.ID[0]] = 1 # We'll use 0 as a special flag to not return an instance... but all (at the API level).
    details[V0.UTC_START_DATE[0]] = "2023-08-21"
    details[V0.UTC_START_TIME[0]] = "16:38"                   # Lunch DD'd from JJ's
    details[V0.TOTAL_FAT[0]] = 0          # To be calculated. # #15 Club Tuna(R) (+onions)
    details[V0.TOTAL_CARBOHYDRATE[0]] = 0 # To be calculated. # Chocolate Chip Cookie 
    details[V0.TOTAL_FIBER[0]] = 0        # To be calculated. # Regular Jimmy Chips(R)
    details[V0.TOTAL_PROTEIN[0]] = 0      # To be calculated. # 20oz Bottle Sprite(R)
    details[V0.UTC_STOP_DATE[0]] = "2023-08-21"
    details[V0.UTC_STOP_TIME[0]] = "17:32"
    self.assertTrue(V0.validate(**details))

  def test_new_instance(self):
    tested = V0()
    self.assertEqual(V0.ID[1], tested[V0.ID[0]])
    self.assertEqual(V0.UTC_START_DATE[1], tested[V0.UTC_START_DATE[0]])
    self.assertEqual(V0.UTC_START_TIME[1], tested[V0.UTC_START_TIME[0]])
    self.assertEqual(V0.TOTAL_FAT[1], tested[V0.TOTAL_FAT[0]])
    self.assertEqual(V0.TOTAL_CARBOHYDRATE[1], tested[V0.TOTAL_CARBOHYDRATE[0]])
    self.assertEqual(V0.TOTAL_FIBER[1], tested[V0.TOTAL_FIBER[0]])
    self.assertEqual(V0.TOTAL_PROTEIN[1], tested[V0.TOTAL_PROTEIN[0]])
    self.assertEqual(V0.UTC_STOP_DATE[1], tested[V0.UTC_STOP_DATE[0]])
    self.assertEqual(V0.UTC_STOP_TIME[1], tested[V0.UTC_STOP_TIME[0]])

