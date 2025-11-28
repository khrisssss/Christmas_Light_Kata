# Define the function to apply each instruction
def update_lights(light_grid, command_text):
    words = command_text.split()
    if words[0] == "toggle":
        action = "toggle"
        start = tuple(map(int, words[1].split(",")))
        end = tuple(map(int, words[3].split(",")))
    else:
        action = words[1]  # "on" or "off"
        start = tuple(map(int, words[2].split(",")))
        end = tuple(map(int, words[4].split(",")))

    for row in range(start[0], end[0] + 1):
        for col in range(start[1], end[1] + 1):
            if action == "on":
                light_grid[row][col] = 1
            elif action == "off":
                light_grid[row][col] = 0
            elif action == "toggle":
                light_grid[row][col] = 1 - light_grid[row][col]


# Create the grid (1000 x 1000 lights, all OFF)
light_grid = [[0 for _ in range(1000)] for _ in range(1000)]

# This line read instructions from the examples_input.txt
with open("examples_input.txt") as f:
    for line in f:
        update_lights(light_grid, line.strip())

# This line count how many lights are ON
lights_on = sum(sum(row) for row in light_grid)
print("Lights on:", lights_on)
