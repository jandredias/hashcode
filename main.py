#main.py
LIVRE = 0
ARMAZEM = 1

#preencher mapa

grid = []
line = input()
words = line.split()
print(words)

for e in range(int(words[0])):
  aux = []
  for i in range(int(words[1])):
    aux += [LIVRE]
  grid += aux

# 0 => posicao vazia

nr_drones = int(words[2])
turns = int(words[3])
max_payload = int(words[4])

nr_types = int(input())

string = input()
weigh = string.split()

print(weigh)

