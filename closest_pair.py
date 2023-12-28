'''
#Karthik Sridhar ICP extra credit Assignment
#Citation:
https://www.geeksforgeeks.org/closest-pair-of-points-using-divide-and-conquer-algorith
m/
#Problem:
# Given a set of points in a plane, p = {(x0, y0),(x1, y1), . . . ,(xn−1, yn−1)},
consider the problem of determining the closest pair of points; i.e., pairs
pi = (xip, yi) and pj = (xj , yj ) such that the distance between them dij = (xi − xj
)2 + (yi − yj )
'''

import math

class point():
  def __init__(self, x, y):
    self.x = x
    self.y = y

  def __repr__(self):
    return f"({self.x}, {self.y})"

def distance(p1, p2):
    return math.sqrt((p1.x - p2.x) ** 2 + (p1.y - p2.y) ** 2)

def compareAll(Arr, n):
  min_val = (None, None, float('inf'))
  for i in range(n):
    for j in range(i + 1, n):
      if distance(Arr[i], Arr[j]) < min_val[2]:
        min_val = (Arr[i], Arr[j], distance(Arr[i], Arr[j]))

  return min_val

def recursiveSearch(Arr, n):

  if n <= 3:
    return compareAll(Arr, n)

  mid = n // 2
  midPoint = Arr[mid]
  L = Arr[:mid]
  R = Arr[mid:]
  dl = recursiveSearch(L, mid)
  dr = recursiveSearch(R, n - mid)
  d = min(dl,dr, key = lambda x : x[2])
  stripP = []
  for i in range(n):
    if abs(Arr[i].x - midPoint.x) < d[2]:
      stripP.append(Arr[i])
  stripP.sort(key = lambda point: point.y)

  for i in range(len(stripP)):
    for j in range(i+1, min(len(stripP), i+8)):
      this_pair = (stripP[i], stripP[j], distance(stripP[i], stripP[j]))
      if(this_pair[2] < d[2]):
        d = this_pair

  return d

def closestPair(Arr, n):
  Arr.sort(key = lambda point: point.x)
  return recursiveSearch(Arr, n)

Arr = [point(10, 13), point(17, 5), point(4, 16), point(19, 51), point(5, 15),
point(6, 19)]
n = len(Arr)
print("The closest pair of points are:", closestPair(Arr, n))