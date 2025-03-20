ogr2ogr -f "PostgreSQL" PG:"dbname=cascadia_gis user=postgres" cities.shp -nln cascadia_city -append
