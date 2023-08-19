

class Model:
  def onVersionedValidation(self, version, **details):
    return False

  def validate_unversioned(self, **details):
    return False

  def validate(self, **details):
    validated = False

    if "version" in details:
      version = details.pop("version")
      validated = self.onVersionedValidation(version, **details)
    else:
      validated = self.validate_unversioned(**details)

    return validated

