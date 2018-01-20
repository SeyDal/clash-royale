s = """E 1 0 0 E
0 1 1 E 1
1 1 0 0 0
E 0 0 A 0
1 1 0 1 0"""


width = 5
height = 5


#input
lines = s.split ("\n")
inp = []
for line in lines:
  inp.append(line.split(" "))


#finding_start
for i in range (height):
  for j in range (width):
    if inp[i][j]=="A":
      start = (i,j)
      break

#making graph:
graph = [[[] for j in range(width)]for i in range(height)]
for i in range (height):
  for j in range (width):
    if inp[i][j] == "1":
      continue
    if i-1 >=0:
      if inp[i-1][j] != "1":
        graph[i][j].append((i-1,j))
    if j-1 >=0:
      if inp[i][j-1] != "1":
        graph[i][j].append((i,j-1))
    if i+1 < height: 
      if inp[i+1][j] != "1":
        graph[i][j].append((i+1,j))
    if j+1 <width: 
      if inp[i][j+1] != "1":
        graph[i][j].append((i,j+1))


#bfs

parent = [[None for j in range(width)]for i in range(height)]


width = 5
height = 5


#input
lines = s.split ("\n")
inp = []
for line in lines:
  inp.append(line.split(" "))


#finding_start
for i in range (height):
  for j in range (width):
    if inp[i][j]=="A":
      start = (i,j)
      break

#making graph:
graph = [[[] for j in range(width)]for i in range(height)]
for i in range (height):
  for j in range (width):
    if inp[i][j] == "1":
      continue
    if i-1 >=0:
      if inp[i-1][j] != "1":
        graph[i][j].append((i-1,j))
    if j-1 >=0:
      if inp[i][j-1] != "1":
        graph[i][j].append((i,j-1))
    if i+1 < height: 
      if inp[i+1][j] != "1":
        graph[i][j].append((i+1,j))
    if j+1 <width: 
      if inp[i][j+1] != "1":
        graph[i][j].append((i,j+1))


#bfs

parent = [[None for j in range(width)]for i in range(height)]
marked = [[False for j in range(width)]for i in range(height)]

Q = [start]
end = None
found = False
marked[start[0]][start[1]] = True
while len(Q)>0 and not found:
  current = Q.pop(0)
  marked [current[0]][current[1]] = True
  for neighbour in graph[current[0]][current[1]]:
    if inp[neighbour[0]][neighbour[1]] == "E":
      parent[neighbour[0]][neighbour[1]] = current
      end = neighbour
      found = True
      break
    elif not marked[neighbour[0]][neighbour[1]]:
      parent[neighbour[0]][neighbour[1]] = current
      Q.append(neighbour)

#printing path
path = []
while end != start:
  path.append(end)
  end = parent[end[0]][end[1]]
path.append(start)
print(path[-2])
for element in path[::-1]:
  print (element[0]+1,element[1]+1)

