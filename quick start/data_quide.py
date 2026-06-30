import rasterio
import numpy as np
import matplotlib.pyplot as plt

path = r"D:\isro\ps-8_moon_data_dem\data\data\derived\20211113\ch2_tmc_ndn_20211113T0855227665_d_dtm_d18.tif"

with rasterio.open(path) as src:

    print("=" * 70)
    print("CHANDRAYAAN-2 DTM INFORMATION")
    print("=" * 70)

    print(f"Driver              : {src.driver}")
    print(f"Width               : {src.width}")
    print(f"Height              : {src.height}")
    print(f"Bands               : {src.count}")
    print(f"Data Type           : {src.dtypes[0]}")
    print(f"NoData Value        : {src.nodata}")
    print(f"Coordinate System   : {src.crs}")
    print(f"Bounds              : {src.bounds}")
    print(f"Transform           :")
    print(src.transform)
    print()

    print("Reading overview...")
    img = src.read(1, out_shape=(1200, 1200))

# Convert to float
img = img.astype(np.float32)

# Replace NoData with NaN
img[img == -32768] = np.nan

print("=" * 70)
print("OVERVIEW STATISTICS")
print("=" * 70)

print(f"Overview Shape      : {img.shape}")
print(f"Minimum Elevation   : {np.nanmin(img):.2f} m")
print(f"Maximum Elevation   : {np.nanmax(img):.2f} m")
print(f"Mean Elevation      : {np.nanmean(img):.2f} m")
print(f"Median Elevation    : {np.nanmedian(img):.2f} m")
print(f"Std Deviation       : {np.nanstd(img):.2f} m")

valid_pixels = np.count_nonzero(~np.isnan(img))
nodata_pixels = np.count_nonzero(np.isnan(img))
total_pixels = img.size

print(f"Valid Pixels        : {valid_pixels:,}")
print(f"NoData Pixels       : {nodata_pixels:,}")
print(f"Total Pixels        : {total_pixels:,}")

print(f"Valid Percentage    : {(valid_pixels/total_pixels)*100:.2f}%")
print(f"NoData Percentage   : {(nodata_pixels/total_pixels)*100:.2f}%")

print("=" * 70)

plt.figure(figsize=(14, 8))

plt.imshow(
    img,
    cmap="terrain",
    vmin=np.nanmin(img),
    vmax=np.nanmax(img)
)

plt.colorbar(label="Elevation (m)")
plt.title("Chandrayaan-2 DTM Overview")

plt.show()
