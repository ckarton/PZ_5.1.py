try:
  veg = {'чай', 'виноград', 'хмель', 'бахча', 'табак','овёс'}
  wg1 = {'чай','табак','овёс'}
  wg2 = {'бахча','табак','хмель'}
  wg3 = {'хмель','табак','виноград'}
  print("В каждом колхозе есть ", veg & wg1 & wg2 & wg3)
  print("Хотябы в 1 колхозе есть ", veg | gw1 | wg2 | wg3)
except:
  print("что-то не так")