#main.py
#FREE = 0
#WAREHOUSES = 1

#preencher mapa
from drone import Drone
from warehouse import Warehouse 
from order import Order
import copy
from manager import Manager

line = input()
words = line.split()

class load:
  def __init__(self, w, p, a):
    self._idOfWarehouse = w
    self._idOfProduct = p
    self._amountRetrieved = a

  def setWarehouse(self, id):
    self._idOfWarehouse = id

  def setProduct(self, id):
    self._idOfProduct = id

  def setAmount(self, am):
    self._amountRetrieved = am

  def getWarehouse(self):
    return self._idOfWarehouse

  def getProduct(self):
    return self._idOfProduct

  def getAmount(self):
    return self._amountRetrieved


####
def deliveryCalculateStorageVisit(orderList, warehouseList):
  numberOfProducts = manager.numberOfTypes()
  requiredToVisit = []
  localWarehouseList = copy.deepcopy(warehouseList)
  #iterate over all orders
  orderIteration=0
  for i in orderList:
    # Replace with the name of the variable, this assumes that if the amount desired is 0 it will still be in the list
    # iterate over all products of that order
    tempRequired = []
    requiredAmountOfProduct = [0 for x in range(numberOfProducts)]
    print(type(i.products()))
    for key in i.products():
      value = i.products()[key]
      requiredAmountOfProduct[key] = value
      if requiredAmountOfProduct[key] != 0:
        requiredAmount = requiredAmountOfProduct[key]
        currentAmount = 0
        warehouseIndex = 0
        # iterate over all warehouses to check if they have the amount required
        for w in i.closeWarehouses():
          amountInStorage = w.quantity(key)
          if amountInStorage != 0:
            currentAmount += amountInStorage
          
          if currentAmount >= requiredAmount:
            w.removeQuantity(key, amountInStorage - (currentAmount - requiredAmount))
            tempRequired.append(load(WAREHOUSENUMBER,key, amountInStorage - (currentAmount - requiredAmount)))
            break
          if amountInStorage != 0:
            w.removeQuantity(key, amountInStorage)
            tempRequired.append(load(WAREHOUSENUMBER,key, amountInStorage))
          warehouseIndex += 1
    requiredToVisit.append(tempRequired)
    orderIteration += 1
  print(requiredToVisit)
  return requiredToVisit

##########



'''grid = []
for e in range(int(words[0])):
  aux = []
  for i in range(int(words[1])):
    aux += [FREE]
  grid += aux
'''
nr_drones = int(words[2])
turns = int(words[3])
max_payload = int(words[4])
manager = Manager()
manager.changeDrones(int(words[2]))
manager.changeTurns(int(words[3]))
manager.changePayload(int(words[4]))

manager.changeNumberOfTypes(int(input()))

manager.changeWeigh(input().split())

for e in range(int(input())):
  #creates all warehouses
  w = Warehouse(input().split())
  w.addproducts(input().split())
  manager.addWarehouse(w)

nr_orders = int(input())

orders = []
for e in range(nr_orders):
  order = Order(len(orders), input().split())
  order.addproducts(int(input()), input().split())
  manager.addOrder(order)

manager.organizeWarehouses()

#for e in orders:
#  print(e.products())

deliveryCalculateStorageVisit(manager.orders(), manager.warehouses())
