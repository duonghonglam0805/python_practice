# Enter your code here. Read input from STDIN. Print output to STDOUT
def find_captains_room(k, room_list):
    room_count = {}
    for room in room_list:
        room_count[room] = room_count.get(room, 0) + 1
    
    for room, count in room_count.items():
        if count != k:
            return room

k = int(input())
room_list = list(input().split())
print(find_captains_room(k, room_list))
