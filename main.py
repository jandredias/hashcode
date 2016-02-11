#main.py
#FREE = 0
#WAREHOUSES = 1

#preencher mapa
from warehouse import Warehouse 
from order import Order
from manager import Manager

line = input()
words = line.split()

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

