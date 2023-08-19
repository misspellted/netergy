

from models import Model


class StoredEnergy(Model):
  ID = "id"
  UTC_DATE = "utc_date"
  UTC_TIME = "utc_time"
  TOTAL_BODY_WEIGHT = "total_body_weight"
  BODY_FAT_PERCENT = "body_fat_percent"

  # If we... define the keys above... what's really stopping us from dumping the values
  # into the parent Model class? Shiiit... we could even make 'em tuples, the second
  # value being a default for a new instance!

  def __init__(self):
    self.id = -1
    self.utc_date = None
    self.utc_time = None
    self.total_body_weight = -1
    self.body_fat_percent = -1

  @classmethod
  def validate(_, **details):
    fields = dict()

    for field in [
      StoredEnergy.ID,
      StoredEnergy.UTC_DATE,
      StoredEnergy.UTC_TIME,
      StoredEnergy.TOTAL_BODY_WEIGHT,
      StoredEnergy.BODY_FAT_PERCENT
    ]:
      fields[field] = details.get(field, None)

    return not None in fields.values()

