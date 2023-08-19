

from models import Model
from stored.v0 import StoredEnergy as V0


class StoredEnergy(Model):
  def __init__(self):
    print("oh hai")
    self.versions = dict()
    self.versions["v0"] = V0

  def onVersionedValidation(self, version, **details):
    validated = False

    if version in self.versions:
      validated = self.versions[version].validate(**details)

    return validated

  def validate_unversioned(self, **details):
    validated = False

    # TODO: Figure... something... out?

    return validated

