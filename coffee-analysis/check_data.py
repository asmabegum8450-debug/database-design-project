import pandas as pd

exports = pd.read_csv("Coffee_export.csv")
imports = pd.read_csv("Coffee_import.csv")
production = pd.read_csv("Coffee_production.csv")

print("\nEXPORT COLUMNS:")
print(exports.columns.tolist())

print("\nIMPORT COLUMNS:")
print(imports.columns.tolist())

print("\nPRODUCTION COLUMNS:")
print(production.columns.tolist())

print("\nEXPORT DATA:")
print(exports.head())

print("\nIMPORT DATA:")
print(imports.head())

print("\nPRODUCTION DATA:")
print(production.head())
