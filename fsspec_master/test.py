import xarray as xr
import intake
import zarr
import numpy as np

cat = intake.open_catalog('catalog.yml')
ds = cat.temp_zip.to_dask()
print(ds)

ds = cat.temp_zipc.to_dask()
print(ds)
