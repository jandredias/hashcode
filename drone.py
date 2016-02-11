class Drone:
  def __init__(self, droneID, location):
    self._id = droneID
    self._location = location
    self._end = 0
    self._orders = []

  def id():
    return self._id

  def location(self):
    return self._location

  def changeLocation(self, location):
    self._location = location

  def end(self):
    return self._end

  def changeEnd(self, end):
    self._end = end

  def orders(self):
    return self._orders

  def addOrders(self, order):
    self._orders += [order]

  def load(self, warehouseID, productID, quantity):
    print(str(self._id) + " L " + str(warehouseID) + " " + str(productID) + " " + str(quantity))

  def unload(self, warehouseID, productID, quantity):
    print(str(self._id) + " U " + str(warehouseID) + " " + str(productID) + " " + str(quantity))

  def deliver(self, warehouseID, productID, quantity):
    print(str(self._id) + " D " + str(warehouseID) + " " + str(productID) + " " + str(quantity))


  def wait(self, turns):
    print(str(self._id) + " W " + str(turns))

