

import unittest
from stored.v0 import StoredEnergy as V0


class TestStoredEnergyV0(unittest.TestCase):
  def test_validate_without_any_detials(self):
    self.assertFalse(V0.validate())

  def test_validate_without_all_detials(self):
    details = dict()
    details[V0.TOTAL_BODY_WEIGHT] = 350
    self.assertFalse(V0.validate(**details))

  def test_validate_with_all_detials(self):
    details = dict()
    details[V0.ID] = 0
    details[V0.UTC_DATE] = "2023-08-18"
    details[V0.UTC_TIME] = "12:21"
    details[V0.TOTAL_BODY_WEIGHT] = 348
    details[V0.BODY_FAT_PERCENT] = 46.51
    self.assertTrue(V0.validate(**details))

