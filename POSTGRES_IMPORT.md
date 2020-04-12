# Postgres with postgis 3

```
docker run -v heightmap-data:/var/lib/postgresql/data -e POSTGRES_PASSWORD=postgres --name postgis -p 5433:5432 postgis/postgis:12-3.0

# password is postgres
psql -h127.0.0.1 -p5433 -dpostgres -Upostgres
create extension postgis_raster;
CREATE EXTENSION postgis_sfcgal;
```

# SQL from HGT files

```
cd /Volumes/General-1/srtm/version2_1/SRTM3/Eurasia
raster2pgsql -s 4236 -d -F -I -C -b 1 \
    N40W007.hgt.zip \
    N40W008.hgt.zip \
    N39W007.hgt.zip \
    N39W008.hgt.zip \
    public.heightmap \
    | psql -h127.0.0.1 -p5433 -dpostgres -Upostgres
```

# Load into postgres

```
# Passsord is "postgres" (set in docker run command above)
cat central_portugal.sql | psql -h127.0.0.1 -p5433 -dpostgres -Upostgres
```