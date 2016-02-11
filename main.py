#main.py
#FREE = 0
#WAREHOUSES = 1

#preencher mapa
from warehouse import Warehouse 
from order import Order
import copy

line = input()
words = line.split()
#print(words)


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
    for a in range(0, numberOfProducts):
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

nr_types = int(input())

string = input()
weigh = string.split()

nr_warehouses = int(input())
warehouses = []

for e in range(nr_warehouses):
  w = Warehouse(input().split())
  w.addproducts(input().split())

nr_orders = int(input())

orders = []
for e in range(nr_orders):
  order = Order(len(orders), input().split())
  order.addproducts(int(input()), input().split())
  orders += [order]

#for e in orders:
#  print(e.products())

deliveryCalculateStorageVisit(orders, warehouses)


