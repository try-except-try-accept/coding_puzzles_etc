from random import randint

HEIGHT = randint(3, 10)

def random_triangle():
     '''Create a random triangle of digits'''
     triangle = ''
     
     buffer = (HEIGHT+1//2)     
     for i in range(HEIGHT):       
          triangle += buffer * " "
          buffer -= 1
          for j in range(i+1):
               n = randint(0, 9)
               triangle += str(n) + " "
          triangle += "\n"                   
          
     return triangle

test_data = random_triangle()

print("Testing ... ")
print(test_data)

# convert into data we can actually use
triangle = [row.strip().split() for row in test_data.strip().split("\n")]
depth = HEIGHT - 1

# find all possible binary (left? or right?) pathways
possible_paths = [bin(num)[2:].zfill(depth) for num in range(0, 2**depth)]

traversals = [[]]

attempts = 0
best = [0]

for path in possible_paths:
     traversals.append([int(triangle[0][0])]) # start from top of triangle
     current = 0
     level = 1          
     for turn in path:
          
          if int(turn):
               current += 1

          traversals[-1].append(int(triangle[level][current]))
          level += 1

     if sum(traversals[-1]) > sum(best):
          best = traversals[-1]

     attempts += 1
    

print("Best path is: ", best, sum(best))
     





          

          
     
