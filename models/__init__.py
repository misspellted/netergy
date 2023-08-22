

class Model:
  def __init__(self, fields=[]):
    """
    `fields` is expected to be a list of tuples, each being the pair of the name of the field, and the second the default value on instantiation.
    """
    self.fields = dict()

    for field in fields:
      self.fields[field[0]] = field[1]

  def __getitem__(self, field):
    return self.fields[field]

  def __setitem__(self, field, value):
    # But only if the field already exists.
    if field in self.fields:
      self.fields[field] = value

  def onVersionedValidation(self, version, **details):
    return False

  def onUnversionedValidation(self, **details):
    return False

  def validate(self, **details):
    validated = False

    if "version" in details:
      version = details.pop("version")
      validated = self.onVersionedValidation(version, **details)
    else:
      validated = self.onUnversionedValidation(**details)

    return validated

