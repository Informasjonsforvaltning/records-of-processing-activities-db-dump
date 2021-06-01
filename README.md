# records-of-processing-activities-etl

## Extract
```
% db.organisations.find()  # db_organisations.json
% db.records.find()  # db_records.json
```

## Install and run extract
```
% poetry shell
% cd extract
% python extract_mongodb_data.py
```
## Install and run notebook
```
% poetry install
% poetry shell
% jupyter notebook
```

## Environment
```
MONGO_HOST=localhost
MONGO_PORT=27017
MONGO_USERNAME=admin
MONGO_PASSWORD=secret
MONGO_DB=records-of-processing-activities
```
