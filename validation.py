#validation script for validating detection rule toml files for elastic

import tomllib
import sys

file = "alert_example.toml"

with open(file, "rb") as toml:
    alert = tomllib.load(toml)

required_fields = ['description', 'name', 'risk_score', 'severity', 'type', 'query']
present_fields = []
missing_fields = []

for table in alert:
    for field in alert[table]:
        present_fields.append(field)

for field in required_fields:
    if field not in present_fields:
        missing_fields.append(field)


print(required_fields)
print("\n")
print(present_fields)
print("\n")
print(missing_fields)
