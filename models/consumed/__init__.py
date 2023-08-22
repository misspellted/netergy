

from models import Model
from models.consumed.v0 import ConsumedEnergy as V0


class ConsumedEnergy(Model):
  def __init__(self):
    print("oh hai")
    self.versions = dict()
    self.versions["v0"] = V0

  def onVersionedValidation(self, version, **details):
    validated = False

    if version in self.versions:
      validated = self.versions[version].validate(**details)

    return validated

  def onUnversionedValidation(self, **details):
    validated = False

    # TODO: Figure... something... out?

    return validated

