

import unittest
from models.stored.v0 import StoredEnergy as V0


class TestStoredEnergyV0(unittest.TestCase):
  def test_validate_without_any_detials(self):
    self.assertFalse(V0.validate())

  def test_validate_with_empty_detials(self):
    details = dict()
    self.assertFalse(V0.validate(**details))

  def test_validate_without_all_detials(self):
    details = dict()
    details[V0.TOTAL_BODY_WEIGHT[0]] = 250  # I'd be ecstatic to be at 250 lbs!
    details[V0.BODY_WEIGHT_UNIT[0]] = "lbs" # Oh yeah, probably best to not assume pounds, so store that too!
    details[V0.BODY_FAT_PERCENT[0]] = 25.00 # Still higher than "fit", but better than nearly fuckin' half!
    self.assertFalse(V0.validate(**details))

  def test_validate_with_all_detials(self):
    details = dict()
    details[V0.ID[0]] = 1 # We'll use 0 as a special flag to not return an instance... but all (at the API level).
    details[V0.UTC_DATE[0]] = "2023-08-18"              # And yeah... _sigh_
    details[V0.UTC_TIME[0]] = "12:21"                   # These are real numbers.
    details[V0.TOTAL_BODY_WEIGHT[0]] = 348              # That's what prompted me to really start working on this
    details[V0.BODY_WEIGHT_UNIT[0]] = "lbs"             # Oh yeah, probably best to not assume pounds, so store that too!
    details[V0.BODY_FAT_PERCENT[0]] = 46.51             # To find a better shape than 'super ultra mega morbidly obese'.
    details[V0.MEASUREMENT_DEVICE[0]] = "FitBit Aria 2" # Because I have one, and finally doing something other than uploading data.
    self.assertTrue(V0.validate(**details))

  def test_new_instance(self):
    tested = V0()
    self.assertEqual(V0.ID[1], tested[V0.ID[0]])
    self.assertEqual(V0.UTC_DATE[1], tested[V0.UTC_DATE[0]])
    self.assertEqual(V0.UTC_TIME[1], tested[V0.UTC_TIME[0]])
    self.assertEqual(V0.TOTAL_BODY_WEIGHT[1], tested[V0.TOTAL_BODY_WEIGHT[0]])
    self.assertEqual(V0.BODY_WEIGHT_UNIT[1], tested[V0.BODY_WEIGHT_UNIT[0]])
    self.assertEqual(V0.BODY_FAT_PERCENT[1], tested[V0.BODY_FAT_PERCENT[0]])
    self.assertEqual(V0.MEASUREMENT_DEVICE[1], tested[V0.MEASUREMENT_DEVICE[0]])

