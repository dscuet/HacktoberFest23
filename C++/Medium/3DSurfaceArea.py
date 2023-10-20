# Read input values
height, width = map(int, input().split())
board = []
for _ in range(height):
    row = list(map(int, input().split()))
    board.append(row)

# Initialize the total surface area
surface_area = 0

# Iterate through the board and calculate the surface area for each cell
for i in range(height):
    for j in range(width):
        cell_height = board[i][j]
        
        # Calculate the top and bottom areas
        top_bottom_area = 2 if cell_height > 0 else 0
        
        # Calculate the side areas by checking adjacent cells
        left_height = 0 if j == 0 else board[i][j - 1]
        right_height = 0 if j == width - 1 else board[i][j + 1]
        up_height = 0 if i == 0 else board[i - 1][j]
        down_height = 0 if i == height - 1 else board[i + 1][j]
        
        side_area = max(0, cell_height - left_height) + max(0, cell_height - right_height) + max(0, cell_height - up_height) + max(0, cell_height - down_height)
        
        # Add the calculated areas to the total surface area
        surface_area += top_bottom_area + side_area

# Calculate the total price of the toy
price = surface_area

# Print the price of the toy
print(price)
