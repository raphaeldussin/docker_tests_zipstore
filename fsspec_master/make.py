import xarray as xr
import zarr
import numpy as np

ds = xr.Dataset()
ds['lon'] = xr.DataArray(data=np.arange(360), dims=('lon'))
ds['lat'] = xr.DataArray(data=np.arange(-90,90), dims=('lat'))
ds['temp'] = xr.DataArray(data=np.random.rand(180, 360), dims=('lat', 'lon'))

store = zarr.ZipStore('temp_zip.zip', mode='w')
ds.to_zarr(store, consolidated=False, mode='w')
store.close()

store = zarr.ZipStore('temp_zipc.zip', mode='w')
ds.to_zarr(store, consolidated=True, mode='w')
store.close()
