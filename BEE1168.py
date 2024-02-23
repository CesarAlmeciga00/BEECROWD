def led(n):
    count = 0;
    listLed = []
    leds ={
    0:6,
    1:2,
    2:5,
    3:5,
    4:4,
    5:5,
    6:6,
    7:3,
    8:7,
    9:6
    }
    for i in range(len(n)):
        listLed.append(leds[int(n[i])])
    
    
    for i in range(len(listLed)):
       count+=listLed[i]
    
    return count



if __name__ == '__main__':
  cases = int(input())
  for i in range(cases):
    try:
      n = input()
      print(f"{led(n)} leds")
    except EOFError:
      break
    