aquarium_length = int(input())
aquarium_width = int(input())
aquarium_height = int(input())
percentage = float(input())

aquarium_volume = aquarium_length * aquarium_width * aquarium_height
aquarium_volume_liters = aquarium_volume * 0.001

liters_needed = aquarium_volume_liters * (1 - (percentage / 100))
print(liters_needed)