# cascadia_gis
GIS for Cascadia

## Data Management

```
./manage.py dumpdata --indent 2 cascadia > cascadia/fixtures/data.json
./manage.py loaddata cascadia/fixtures/data.json 
```

## Cascadia Resources
 - https://cascadia-institute.org
 - https://cascadiabioregion.org
 - https://regeneratecascadia.org
 - https://cascadia.ecotopia.today/

 ## UV Tips
 ```
 uv venv
 source .venv/bin/activate
 uv install
 uv run --env-file .env ./manage.py shell
 uv run --env-file .env ./manage.py runserver
 uv pip freeze > requirements.txt
