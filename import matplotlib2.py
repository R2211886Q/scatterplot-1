import matplotlib.pyplot as plt

def plot_data():
    # Define the x and y coordinates
    x_coords = []
    y_coords = []
    
    # Open the coordinate file using the 'read' (r) mode
    file_path = 'C:/Users/BresbaneSakala/Desktop/x_y_coordinates.txt'
    my_file = open(file_path, 'r')
    
    # Read the file and extract the coordinates
    for line in my_file:
        x, y = line.strip().split(',')
        try:
            x_coords.append(float(x))
            y_coords.append(float(y))
            print(f'x: {x}, y: {y}')
        except ValueError:
            continue
    
    # Close the file
    my_file.close()

    # Create the scatter plot
    plt.scatter(x_coords, y_coords)
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title('Scatter Plot')
    plt.grid(True)

    # Show the plot
    plt.show()

plot_data()