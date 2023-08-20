

from models import Model


class StoredEnergy(Model):
  ID = ("id", -1)
  UTC_DATE = ("utc_date", None)
  UTC_TIME = ("utc_time", None)
  TOTAL_BODY_WEIGHT = ("total_body_weight", -1.0)
  BODY_WEIGHT_UNIT = ("body_weight_unit", "lbs") # Well, I am a fat American, so... :)
  BODY_FAT_PERCENT = ("body_fat_percent", -1.0)

  def __init__(self):
    Model.__init__(self, [
      StoredEnergy.ID,
      StoredEnergy.UTC_DATE,
      StoredEnergy.UTC_TIME,
      StoredEnergy.TOTAL_BODY_WEIGHT,
      StoredEnergy.BODY_WEIGHT_UNIT,
      StoredEnergy.BODY_FAT_PERCENT
    ])

  @classmethod
  def validate(_, **details):
    fields = dict()

    for field in [
      StoredEnergy.ID[0],
      StoredEnergy.UTC_DATE[0],
      StoredEnergy.UTC_TIME[0],
      StoredEnergy.TOTAL_BODY_WEIGHT[0],
      StoredEnergy.BODY_WEIGHT_UNIT[0],
      StoredEnergy.BODY_FAT_PERCENT[0]
    ]:
      fields[field] = details.get(field, None)

    return not None in fields.values()

