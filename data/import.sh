ogr2ogr -f "PostgreSQL" PG:"dbname=cascadia_gis user=postgres" cities/ne_10m_populated_places.shp -nln cascadia_city -append
