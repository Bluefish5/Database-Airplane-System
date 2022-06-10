class Samolot:
  def __init__(self, zasieg:int, miejsca:int):
    self._zasieg = zasieg
    self._miejsca = miejsca
  
  def get_zasieg(self):
    return self._zasieg
  def get_miejsca(self):
    return self._miejsca
  def __str__(self):
    return type(self).__name__


class Szerokokadlubowy(Samolot):
  def __init__(self):
    super().__init__(8000,250)

class Waskokadlubowy(Samolot):
  def __init__(self):
    super().__init__(2500,150)

class Regionalny(Samolot):
  def __init__(self):
    super().__init__(800, 70)
