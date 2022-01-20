
def translate_to_boolean(value) -> bool:
  if isinstance(value, bool) or isinstance(value, int):
      return bool(value)
  elif isinstance(value, str):
      return value.replace(" ", "").lower() == 'true'