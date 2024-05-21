from PIL import Image

# Load the image
image = Image.open('swift.webp').convert('L')  # Convert to grayscale

# Get pixel values
pixels = list(image.getdata())

# Convert to 2D matrix if needed
width, height = image.size
pixel_matrix = [pixels[i * width:(i + 1) * width] for i in range(height)]


def print_die(val):
    if val == 6:
        print("||||||", end="")
    elif val == 5:
        print("||| ||", end="")
    elif val == 4:
        print("|| || ", end="")
    elif val == 3:
        print("| | | ", end="")
    elif val == 2:
        print(" | |  ", end="")
    elif val == 1:
        print("   |  ", end="")
        
def reduce_to_die(val):
    if val > 0 and val < 51:
        return 1
    elif val > 50 and val < 101:
        return 2
    elif val > 100 and val < 151:
        return 3
    elif val > 150 and val < 201:
        return 4
    elif val > 200 and val < 251:
        return 5
    elif val > 250 and val < 256:
        return 6
    else:
        return 0


index = 0
interval =50
# Print the pixel values
for row in pixel_matrix:
    index += 1
    if index % interval != 0:
        continue
    c = 0
    c_max = len(row)
    
    avg_array = []
    
    while c +interval < c_max:
        sub_array = row[c:c+interval]
        avg_array.append(sum(sub_array) / len(sub_array))
        c += interval
    for val in avg_array:
        print_die(reduce_to_die(val))
    print("\n")


