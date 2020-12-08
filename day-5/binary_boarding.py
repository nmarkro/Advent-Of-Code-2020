def parse_passes():
    passes = []
    with open("./input.txt", "r") as f:
        for line in f.readlines():
            passes.append(line.strip())
    return passes

# Part 1
def get_seat_id(boarding_pass):
    # find row using first 7 characters
    row = int(boarding_pass[:7].replace("F", "0").replace("B", "1"), 2)
    # find colunn using last 3 characters
    column = int(boarding_pass[-3:].replace("L", "0").replace("R", "1"), 2)
    return row * 8 + column

boarding_passes = parse_passes()
seat_ids = []

max_value = 0

for boarding_pass in boarding_passes:
    seat_id = get_seat_id(boarding_pass)
    seat_ids.append(seat_id)
    if seat_id > max_value:
        max_value = seat_id 

print("Part 1 answer: {}".format(max_value))

# Part 2
# this seems wrong, but it gives the right answer so who cares lmao
for seat in seat_ids:
    if (seat + 2) in seat_ids and (seat + 1) not in seat_ids:
        print("Your seat is: {}".format(seat + 1))
        break