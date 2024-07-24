import pandas as pd
from sqlalchemy import create_engine

pokemons = pd.read_csv('data/pokemons.csv')

engine = create_engine('postgresql://postgres:postgres@localhost:5432/pokemons_database')

pokemons.to_sql('pokemons', engine, index=False, if_exists='replace')
