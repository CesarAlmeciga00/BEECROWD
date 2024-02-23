def Main(a, b):
  b = b-1
  listPeople = []
  count = 0
  position = 0
  for i in range(a):
    listPeople.append(i+1)

  while len(listPeople) != 1:
    if count == b:
        try:
            listPeople.pop(position)
            count = 0
        except:
            while position >= len(listPeople):
                position -=  len(listPeople)
            listPeople.pop(position)
            count = 0
    else:
      pass
    count += 1
    position += 1
    if len(listPeople) == 1:
       return listPeople[0]
    else:
       pass
    

if __name__ == '__main__':
  cases = int(input())
  for i in range(cases):
    try:
      a, b = map(int ,input().split())
    except EOFError:
      break
    print(f"Case {i+1}: {Main(a, b)}")