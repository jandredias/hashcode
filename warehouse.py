class Warehouse:
  def __init__(self,loc):
    self._qt = []
    self._location = [int(loc[0]), int(loc[1])]

  def addproducts(self,qt):
    for e in qt:
      self._qt += [int(e)]

  def quantity(self,prodID):
    return self._qt[prodID]

  def location(self):
    return self._location

