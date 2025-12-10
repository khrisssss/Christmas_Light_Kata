# creating a 2D list [0] means OFF
# So grid[0][0] is the top-left light, grid[999][999] is the bottom-right light.
grid = [[0]*1000 for _ in range(1000)]  # total lights 1,000,000 lights


# Instruction from the website of kata
# 1. Turn ON lights in rectangle (887,9) through (959,629)
for r in range(887, 960):       # rows 887 … 959
    for c in range(9, 630):     # cols 9 … 629
        # grid[r][c] = True       # set ON  ## This is the PART ONE of the xmas kata##
        # increase brightness by 1 ##This is the PART TWO of the xmas Kata##
        grid[r][c] += 1


# 2. Turn ON lights in rectangle (454,398) through (844,448)
for r in range(454, 845):       # rows 454 … 844
    for c in range(398, 449):   # cols 398 … 448
        # grid[r][c] = True       # set ON  ## This is the PART ONE of the xmas kata##
        # increase brightness by 1   ##This is the PART TWO of the xmas Kata##
        grid[r][c] += 1


# 3. Turn OFF lights in rectangle (539,243) through (559,965)
for r in range(539, 560):       # rows 539 … 559
    for c in range(243, 966):   # cols 243 … 965
        # grid[r][c] = False      # set OFF
        grid[r][c] = max(0, grid[r][c] - 1)   # decrease by 1, but not below 0


# 4. Turn OFF lights in rectangle (370,819) through (676,868)
for r in range(370, 677):       # rows 370 … 676
    for c in range(819, 869):   # cols 819 … 868
        # grid[r][c] = False      # set OFF
        grid[r][c] = max(0, grid[r][c] - 1)


# 5. Turn OFF lights in rectangle (145,40) through (370,997)
for r in range(145, 371):       # rows 145 … 370
    for c in range(40, 998):    # cols 40 … 997
        # grid[r][c] = False      # set OFF
        grid[r][c] = max(0, grid[r][c] - 1)


# 6. Turn OFF lights in rectangle (301,3) through (808,453)
for r in range(301, 809):       # rows 301 … 808
    for c in range(3, 454):     # cols 3 … 453
        # grid[r][c] = False      # set OFF
        grid[r][c] = max(0, grid[r][c] - 1)


# 7. Turn ON lights in rectangle (351,678) through (951,908)
for r in range(351, 952):       # rows 351 … 951
    for c in range(678, 909):   # cols 678 … 908
        # grid[r][c] = True       # set ON
        grid[r][c] += 1         # increase brightness by 1


# 8. TOGGLE lights in rectangle (720,196) through (897,994)
for r in range(720, 898):       # rows 720 … 897
    for c in range(196, 995):   # cols 196 … 994
        # grid[r][c] = not grid[r][c]   # flip ON ↔ OFF
        grid[r][c] += 2         # increase brightness by 2

# 9. TOGGLE lights in rectangle (831,394) through (904,860)
for r in range(831, 905):       # rows 831 … 904
    for c in range(394, 861):   # cols 394 … 860
        # grid[r][c] = not grid[r][c]   # flip ON ↔ OFF
        grid[r][c] += 2         # increase brightness by 2

# Part Two, Calculate total brightness
total_brightness = 0

for r in range(1000):
    for c in range(1000):
        total_brightness += grid[r][c]   # add the brightness of this light

print("Total brightness:", total_brightness)
