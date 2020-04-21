
# one that works

cd fsspec_master
docker build -t debug_xarray-intake:latest .
docker run -it debug_xarray-intake

# not the other

cd fsspec_chained_mapper
docker build -t debug_xarray-intake2:latest .
docker run -it debug_xarray-intake2
