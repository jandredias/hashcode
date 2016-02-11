class Order:
  def __init__(self, dest):
    self._products = {}
    self._destination = [int(dest[0]), int(dest[1])]

  def destination(self):
    return self._destination

  def addproducts(self, qt, prod):
    for e in prod:
      if int(e) in self._products:
        self._products[int(e)] += 1
      else:
        self._products[int(e)] = 1
 
  def quantity(self, prodID):
    return self._products[prodID]

  def products(self):
    return self._products
