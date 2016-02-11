#main.py
#FREE = 0
#WAREHOUSES = 1

#preencher mapa
from warehouse import Warehouse 
from order import Order

line = input()
words = line.split()
#print(words)

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

for e in orders:
  print(e.products())
