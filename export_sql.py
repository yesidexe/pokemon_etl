import pandas as pd
from sqlalchemy import create_engine

engine = create_engine('postgresql://postgres:postgres@localhost:5432/pokemons_database')

query = "SELECT * FROM pokemons WHERE is_strong = 'Es fuerte';"
pokemons_strongest = pd.read_sql_query(query, engine)

# Guarda el DataFrame en un archivo CSV
pokemons_strongest.to_csv('data/pokemons_strongest.csv', index=False)
pokemons_strongest.to_excel('data/pokemons_strongest.xlsx', index=False, engine='openpyxl')