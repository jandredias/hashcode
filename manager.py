import itertools
from drone import Drone
class Manager:
  def __init__(self):
    self._warehouses = []
    self._orders = []
    self._drones = []
    self._turns = 0
    self._weigh = []
    self._payload = 0
    self._types = 0

  def numberOfTypes(self):
    return self._types

  def changeNumberOfTypes(self, number):
    self._types = number

  def payload(self):
    return self._payload

  def changePayload(self, payload):
    self._payload = payload

  def changeTurns(self, turns):
    self._turns = turns

  def turns(self):
    return self._turns

  def changeWeigh(self, w):
    self._weigh = w

  def weigh(self, productID):
    return self._weigh[productID]

  def changeDrones(self, drones):
    i = 0
    for e in range(drones):
      self._drones += [Drone(i, [0,0])]
      i += 1

  def drones(self):
    return self._drones

  def addWarehouse(self, warehouse):
    if 0 == len(self._warehouses):
      for e in self._drones:
        e.changeLocation(warehouse.location())
    self._warehouses += [warehouse]

  def organizeWarehouses(self):
    for e in self._orders:
      e.organizeWarehouses(self._warehouses)

  def addOrder(self, order):
    self._orders += [order]
  def warehouses(self):
    return self._warehouses

  def orders(self):
    return self._orders

  def computeConflicts(self):
    for w in self._warehouses:
      for p in range(self._types):
        orders = w.ordersByProduct(p)
        for perm in itertools.permutations(orders): 
          print()
        #INSERT LEAL STUFF HERE

  def getResults():
    for orders in self._orders:
      drone = self._drones.pop()
      
