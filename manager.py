class Manager:
  def __init__(self):
    self._warehouses = []
    self._orders = []
    self._drones = 0
    self._turns = 0
    self._weigh = []

  def changeTurns(self, turns):
    self._turns = turns

  def turns(self):
    return self._turns

  def changeWeigh(self, w):
    self._weigh = w

  def weigh(self, productID)
    return self._weigh[productID]

  def changeDrones(self, drones):
    self._drones = drones

  def drones(self):
    return self._drones

  def addWarehouse(self, warehouse):
    self._warehouses += [warehouse]

  def addOrder(self, order):
    self._orders += [order]
  def warehouses(self):
    return self._warehouses

  def orders(self):
    return self._orders

 
