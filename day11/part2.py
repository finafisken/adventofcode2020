def look_dir(x_dir, y_dir, pos, seats):
  (x, y) = pos
  char = '.'
  while char == '.':
    x += x_dir
    y += y_dir
    looking_at = (x, y)

    if looking_at not in seats:
      break
    else:
      char = seats.get(looking_at)

  return char

def check_adjecent(pos, seats):
  adjecent_seats = [
   look_dir(-1, 0, pos, seats),
   look_dir(-1, -1, pos, seats),
   look_dir(-1, 1, pos, seats),
   look_dir(1, 0, pos, seats),
   look_dir(1, -1, pos, seats),
   look_dir(1, 1, pos, seats),
   look_dir(0, -1, pos, seats),
   look_dir(0, 1, pos, seats),
  ]

  return adjecent_seats.count('#')

with open('input.txt', 'r') as file:
  data = [r for r in file.read().split('\n')]

  seats_dict = {}
  for y, row in enumerate(data):
    for x, char in enumerate(row):
      seats_dict[(x, y)] = char

  prev_seat_str = ''
  seat_str = ''.join(seats_dict.values())

  while prev_seat_str != seat_str:
    new_seats_dict = {}
    for pos, char in seats_dict.items():
      occupied_adjecent = check_adjecent(pos, seats_dict)
      # seat is empty, no adjecent -> occupied seat
      if char == 'L' and occupied_adjecent == 0:
        new_seats_dict[pos] = '#'
      # seat is occupied, more than 5 adjecent -> empty seat
      elif char == '#' and occupied_adjecent > 4:
        new_seats_dict[pos] = 'L'
      else:
        new_seats_dict[pos] = char
    
    seats_dict = new_seats_dict
    prev_seat_str = seat_str
    seat_str = ''.join(new_seats_dict.values())

  
  print(seat_str.count('#'))