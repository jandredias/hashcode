class Warehouse:
  def __init__(self,loc):
    self._qt = {}
    self._orders = {}
    self._location = [int(loc[0]), int(loc[1])]

  def addproducts(self,qt):
    i = 0
    for e in qt:
      self._qt[i] = [int(e)]
      self._orders[i] = []

  def quantity(self,prodID):
    return self._qt[prodID]

  def location(self):
    return self._location
  
  def addOrder(self, product, order):
    #receives an instance of order and saves the id
    self._orders[productID] += [order.id()]

  def ordersByProduct(self, productID):
    return self._orders[productID]

  def removeQuantity(self, prodID, amount):
    self._qt[prodID] -= amount