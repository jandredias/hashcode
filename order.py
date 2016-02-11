class Order:
  def __init__(self, idNumber, dest):
    self._products = {}
    self._warehouses = {}
    self._id = idNumber
    self._destination = [int(dest[0]), int(dest[1])]
    
  def id(self):
    return self._id;

  def destination(self):
    return self._destination

  def addproducts(self, qt, prod):
    for e in prod:
      if int(e) in self._products:
        self._products[int(e)] += 1
      else:
        self._products[int(e)] = 1
        self._warehouses[int(e)] = []
 
  def setWarehouse(self, productID, warehouseLocation):
    self._warehouses[productID] += [warehouseLocation]

  def warehouse(self, productID):
    return self._warehouses[productID]

  def quantity(self, prodID):
    return self._products[prodID]

  def products(self):
    return self._products
