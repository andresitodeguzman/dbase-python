# DBase for Python
Python port of DBase. Interact with your DBase databse in python. This is still in development so expect a lot of bugs and do not use in production. This not yet stable, use the DBase for PHP instead, visit http://andre.is-great.net/dbase.

## Initialize DBase and the Database
```python
# Import DBase
>>> import DBase

# Initialize
>>> db_sample = db("db_location/db_name")
```

## Operations
1. get - Get a data from the column using a key-value match

```python
>>> sample_value = db_sample.get("column", "key", "value")
```

## Development
- This is still meant for internal usage, download and use with caution and without warranty.
