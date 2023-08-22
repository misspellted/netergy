

from models import Model


class ConsumedEnergy(Model):
  ID = ("id", -1)
  UTC_START_DATE = ("utc_start_date", None)
  UTC_START_TIME = ("utc_start_time", None)
  TOTAL_FAT = ("total_fat", -1.0) # Assumed to be grams.
  TOTAL_CARBOHYDRATES = ("total_carbohydrates", -1.0) # Assumed to be grams.
  TOTAL_FIBER = ("total_fiber", -1.0) # Assumed to be grams.
  TOTAL_PROTEIN = ("total_protein", -1.0) # Assumed to be grams.
  UTC_STOP_DATE = ("utc_stop_date", None)
  UTC_STOP_TIME = ("utc_stop_time", None)
  

  def __init__(self):
    Model.__init__(self, [
      ConsumedEnergy.ID,
      ConsumedEnergy.UTC_START_DATE,
      ConsumedEnergy.UTC_START_TIME,
      ConsumedEnergy.TOTAL_FAT,
      ConsumedEnergy.TOTAL_CARBOHYDRATES,
      ConsumedEnergy.TOTAL_FIBER,
      ConsumedEnergy.TOTAL_PROTEIN,
      ConsumedEnergy.UTC_STOP_DATE,
      ConsumedEnergy.UTC_STOP_TIME
    ])

  @classmethod
  def validate(_, **details):
    fields = dict()

    for field in [
      ConsumedEnergy.ID[0],
      ConsumedEnergy.UTC_START_DATE[0],
      ConsumedEnergy.UTC_START_TIME[0],
      ConsumedEnergy.TOTAL_FAT[0],
      ConsumedEnergy.TOTAL_CARBOHYDRATES[0],
      ConsumedEnergy.TOTAL_FIBER[0],
      ConsumedEnergy.TOTAL_PROTEIN[0],
      ConsumedEnergy.UTC_STOP_DATE[0],
      ConsumedEnergy.UTC_STOP_TIME[0]
    ]:
      fields[field] = details.get(field, None)

    return not None in fields.values()

