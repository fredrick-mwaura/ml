
## feature extraction
import sys
import os

from PIL import Image, ImageFilter

"""
pooling => (downsampling, summarizing or subsampling)
** used to reduce the spatial dimensions of feature maps while retaining essential information
* control model complexity, overfiting, 
types
--------
1. Max pooling - selects max element from a region of feature map covered by the filter
2. Average pooling - Computes the elemnents present in the region of feature map covered by the filter
3. Global pooling - Reduces each channel in the feature map into a single value
    - Global Max Pooling
    - Global average Pooling

convolution - pooling, convolution - pooling (nn)
"""

# Ensure correct usage
if len(sys.argv) != 2:
    sys.exit("Usage: python filter.py crowd.png")

# Open image
image = Image.open(sys.argv[1]).convert("RGB")

# Filter image according to edge detection kernel

# matrix = [[-1, -1, -1],
#           [-1,  8, -1],
#           [-1, -1, -1]]
filtered = image.filter(ImageFilter.Kernel(
    size=(3, 3),  # Kernel size, (width, Height)
    kernel=[-1, -1, -1, -1, 8, -1, -1, -1, -1], # Kernel weights (list rep of the matrix)
    scale=1 # Scale factor - pixels are divided by this val
))

# Save resulting image
saveas = "filtered_image.png"
count = 1
base, ext = os.path.splitext(saveas)
while os.path.exists(saveas):
    saveas = f"{base}_{count}{ext}"
    count += 1
    
filtered.save(saveas)
sys.exit(f"filtered image saved as {saveas}")
