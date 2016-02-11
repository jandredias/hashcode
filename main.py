#main.py
#FREE = 0
#WAREHOUSES = 1

#preencher mapa
from warehouse import Warehouse 
from order import Order
import copy
from manager import Manager

line = input()
words = line.split()

####
def deliveryCalculateStorageVisit(orderList, warehouseList):
  numberOfProducts = len(orderList[0].products())
  requiredToVisit = [[0 for x in range(numberOfProducts)] for x in range(numberOfProducts)] 
  localWarehouseList = copy.deepcopy(warehouseList)
  #iterate over all orders
  for i in orderList:
    # Replace with the name of the variable, this assumes that if the amount desired is 0 it will still be in the list
    # iterate over all products of that order
    requiredAmountOfProduct = []
    for key, value in i.products():
      requiredAmountOfProduct.append(i.quantity(a))
      if requiredAmountOfProduct[a] != 0:
        requiredAmount = requiredAmountOfProduct[a]
        currentAmount = 0
        warehouseIndex = 0
        # iterate over all warehouses to check if they have the amount required
        for w in localWarehouseList:
          amountInStorage = w.quantity(a)
          if amountInStorage != 0:
            currentAmount += amountInStorage
            requiredToVisit[a][warehouseIndex] = 1
          if currentAmount >= requiredAmount:
            w.removeQuantity(a, amountInStorage - (currentAmount - requiredAmount))
            break
          w.removeQuantity(a, amountInStorage)
          warehouseIndex += 1
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

deliveryCalculateStorageVisit(manager.orders, w)
