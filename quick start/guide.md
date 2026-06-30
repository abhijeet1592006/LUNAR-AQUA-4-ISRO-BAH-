
# Reading and Visualizing a Chandrayaan-2 Digital Terrain Model (DTM)

## Objective

The goal of this program is to learn how to open, inspect, process, and visualize a **Chandrayaan-2 Digital Terrain Model (DTM)** using Python.

By the end of this program, you will understand:

- How to read a GeoTIFF file
- How to inspect its metadata
- How to load elevation values into memory
- How to handle missing (NoData) values
- How to compute basic terrain statistics
- How to visualize the terrain as an elevation map

---

# What is a DTM?

A **Digital Terrain Model (DTM)** is a 2D image where each pixel stores the **elevation (height)** of the terrain instead of color.

Unlike a normal image:

- A normal image stores RGB values.
- A DTM stores elevation values.

Example:

| Pixel | Elevation |
|--------|----------:|
| (0,0) | -2100 m |
| (0,1) | -2050 m |
| (0,2) | -2084 m |

This allows us to reconstruct the shape of the Moon's surface.

---

# Libraries Used

```python
import rasterio
import numpy as np
import matplotlib.pyplot as plt
```

## Rasterio

Rasterio is a Python library used to read and write geospatial raster datasets.

It is commonly used for:

- GeoTIFF files
- Satellite imagery
- DEMs
- DTMs
- Remote sensing datasets

Official Documentation

https://rasterio.readthedocs.io/

---

## NumPy

NumPy is the standard Python library for numerical computing.

It allows us to:

- Store elevation values
- Perform mathematical operations
- Handle missing values
- Compute statistics

Official Documentation

https://numpy.org/

---

## Matplotlib

Matplotlib is used for plotting and visualization.

In this program it is used to display the terrain as an image.

Official Documentation

https://matplotlib.org/

---

# Step 1 — Specify the Dataset

```python
path = r"D:\isro\...\ch2_tmc_ndn_20211113T0855227665_d_dtm_d18.tif"
```

This is the path to the Chandrayaan-2 DTM file.

The `r` before the string means **Raw String**.

It tells Python to treat backslashes (`\`) as normal characters instead of escape sequences.

Without it:

```python
"D:\new\data"
```

may produce errors.

Using

```python
r"D:\new\data"
```

avoids this problem.

---

# Step 2 — Open the Dataset

```python
with rasterio.open(path) as src:
```

Rasterio opens the GeoTIFF file.

The variable `src` represents the opened dataset.

The `with` statement automatically closes the file after the block finishes.

This is considered the safest and cleanest way to open files.

---

# Step 3 — Read Dataset Information

```python
print(src.driver)
```

Shows the file format.

Example:

```
GTiff
```

Meaning:

GeoTIFF image.

---

```python
print(src.width)
```

Returns the image width in pixels.

Example:

```
82207
```

---

```python
print(src.height)
```

Returns the image height.

Example:

```
39046
```

---

```python
print(src.count)
```

Returns the number of bands.

A DTM normally contains one band because each pixel stores only elevation.

Example:

```
1
```

---

```python
print(src.dtypes[0])
```

Returns the data type.

Example:

```
int16
```

Meaning:

Each elevation value is stored as a 16-bit integer.

---

```python
print(src.nodata)
```

Returns the NoData value.

Example:

```
-32768
```

Pixels with this value do not contain valid terrain information.

---

```python
print(src.crs)
```

Returns the Coordinate Reference System.

Example:

```
Polar Stereographic
```

This tells us how the Moon's surface is projected onto a flat map.

---

```python
print(src.bounds)
```

Returns the geographic boundaries of the dataset.

It tells us which area of the Moon this file covers.

---

```python
print(src.transform)
```

Returns the affine transformation matrix.

It converts pixel coordinates into real-world coordinates.

It also tells us the spatial resolution.

Example:

```
10 x 10 meters
```

Meaning:

Each pixel represents approximately 10 meters on the Moon.

---

# Step 4 — Read the Elevation Data

```python
img = src.read(1, out_shape=(1200,1200))
```

`read(1)` loads Band 1.

Since a DTM has only one band, Band 1 contains the elevation values.

Instead of loading the full image, we request a smaller preview.

Original size:

```
82207 × 39046
```

Preview size:

```
1200 × 1200
```

This makes the program much faster and uses significantly less memory.

---

# Step 5 — Convert to Floating Point

```python
img = img.astype(np.float32)
```

The original image is stored as integers.

However,

```
NaN
```

(Not a Number)

can only be stored inside floating-point arrays.

Therefore we convert the data to `float32`.

---

# Step 6 — Handle Missing Data

```python
img[img == -32768] = np.nan
```

The dataset uses

```
-32768
```

to indicate missing data.

These pixels do not represent terrain.

Replacing them with

```
NaN
```

allows NumPy to ignore them during calculations.

Without this step, statistics would be incorrect.

---

# Step 7 — Compute Terrain Statistics

The following functions ignore all NaN values.

## Minimum Elevation

```python
np.nanmin(img)
```

Returns the lowest valid elevation.

---

## Maximum Elevation

```python
np.nanmax(img)
```

Returns the highest elevation.

---

## Mean Elevation

```python
np.nanmean(img)
```

Computes the average terrain height.

---

## Median Elevation

```python
np.nanmedian(img)
```

Returns the middle elevation value.

---

## Standard Deviation

```python
np.nanstd(img)
```

Measures how much the terrain elevations vary.

Large values indicate rough terrain.

Small values indicate smoother terrain.

---

# Step 8 — Count Valid Pixels

```python
valid_pixels = np.count_nonzero(~np.isnan(img))
```

Counts pixels containing valid elevation data.

---

```python
nodata_pixels = np.count_nonzero(np.isnan(img))
```

Counts missing pixels.

---

```python
total_pixels = img.size
```

Returns the total number of pixels.

---

The percentages are calculated as:

```python
(valid_pixels / total_pixels) * 100
```

and

```python
(nodata_pixels / total_pixels) * 100
```

This tells us how much of the preview actually contains terrain.

---

# Step 9 — Visualize the Terrain

```python
plt.figure(figsize=(14,8))
```

Creates a new figure.

The size is measured in inches.

---

```python
plt.imshow(...)
```

Displays the elevation map.

---

```python
cmap="terrain"
```

Applies the Terrain color map.

Typical colors:

- Dark Blue → Lowest elevation
- Green → Medium elevation
- Brown → High elevation
- White → Highest elevation

---

```python
vmin=np.nanmin(img)
vmax=np.nanmax(img)
```

Maps the full elevation range to the color scale.

---

```python
plt.colorbar(label="Elevation (m)")
```

Adds a color scale showing elevation in meters.

---

```python
plt.title(...)
```

Adds a title to the figure.

---

```python
plt.show()
```

Displays the visualization.

---

# Program Workflow

```text
GeoTIFF File
      │
      ▼
Open Dataset
      │
      ▼
Read Metadata
      │
      ▼
Load Elevation Data
      │
      ▼
Convert to Float
      │
      ▼
Replace NoData with NaN
      │
      ▼
Compute Statistics
      │
      ▼
Visualize Terrain
```

---

# Output

After running the program, you will obtain:

- Dataset information
- Image dimensions
- Coordinate system
- Pixel resolution
- Elevation statistics
- Percentage of valid terrain
- A terrain visualization with elevation colors

---



BY ABHIJEET SINGH
Delhi,India
abhijeet8800434205@gmail.com


