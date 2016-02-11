import math
order_location = []
class Order:
  def __init__(self, idNumber, dest):
    self._products = {}
    self._warehouses = {}
    self._warehousesByDistance = []
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

  def organizeWarehouses(self, warehouses):
    global order_location
    order_location = self._destination
    for e in warehouses:
      self._warehousesByDistance += [e]
    self._warehousesByDistance.sort(key=distance)
    print("ORDER")
    for e in self._warehousesByDistance:
      print(e.location())

def distance(o):
  return math.sqrt(pow(o.location()[0] - order_location[0], 2) + pow(o.location()[1] - order_location[1],2))

