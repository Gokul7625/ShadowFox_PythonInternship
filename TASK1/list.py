# TASK 1_list
J_league = ["Superman", "Batman", "Wonder Woman", "Flash", "Aquaman", "Green Lantern"]

# 1. Calculate the no_members
no_members = len(J_league)
print(f"No_members: {no_members}")

# 2. Add them to the list
J_league.append("Batgirl")
J_league.append("Nightwing")
print(f"adding new members: {J_league}")

# 3.Move her to the beginning of the list
J_league.remove("Wonder Woman")
J_league.insert(0, "Wonder Woman")
print(f"Wonder Woman as the leader: {J_league}")

# 4. Separate Aquaman and Flash by moving either "Green Lantern" or "Superman" between them
J_league.remove("Green Lantern")
aquaman_index = J_league.index("Aquaman")
J_league.insert(aquaman_index + 1, "Green Lantern")
print(f"After_separating: {J_league}")

# 5. Replace
J_league = ["Cyborg", "Shazam", "Hawkgirl", "Martian Manhunter", "Green Arrow"]
print(f"New_members: {J_league}")

# 6. Sort
J_league.sort()
new_leader = J_league[0]
print(f"Sorted_order: {J_league}")
print(f"leader: {new_leader}")
