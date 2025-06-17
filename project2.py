import pandas as pd 
import logging 
from sqlalchemy import create_engine,text
from sqlalchemy.exc import ResourceClosedError
import time
import requests
import json

''' configuring format of the logging and crating engine '''

logging.basicConfig(
    level=logging.DEBUG,
    filename='logs/project2.log',
    format='%(asctime)s-%(levelname)s-%(message)s',
    filemode="a"
)

con_string="mysql+pymysql://root:tanishk@localhost/project2"
engine=create_engine(con_string)

''' creating database for project'''

def create_datbase():
    
    queries='''drop database if exists project2;
           create database project2;'''
    
    try:
        part=queries.strip().split(";")
        part=[p.strip() for p in part if p.strip()]
        for query in part:
            with engine.begin() as conn:
                conn.execute(text(query))
                logging.info(f"executed query{query}")
        print("query successfully executed")
    except ResourceClosedError:
        logging.warning("Executed, but no rows to return.")
    logging.info('database successfully created')

def ingest_db(df,table,engine):
    df.to_sql(table,con=engine,if_exists="append",index=False)

def work_db():
    
    start=time.time()
    all_pokemon=[]
    data=[]
    
    url = "https://pokeapi.co/api/v2/pokemon/"
    while url:
        response = requests.get(url).json()
        all_pokemon.extend(response["results"])
        url = response["next"]  # Move to next page
        
    for info in all_pokemon:
        name = info['name']
        pokemon_detail_url = f'https://pokeapi.co/api/v2/pokemon/{name}'
        request = requests.get(pokemon_detail_url)
        
        if request.status_code !=200:
            logging.warning(f"data not found for Pokemon = {name} at {pokemon_detail_url}")
            continue

        details=request.json()

        ''' Build structured dictionary'''
        
        data.append({
            "id":details["id"],
            "name": details["forms"][0]["name"],
            "base_experience": details["base_experience"],
            "height": details["height"],
            "weight": details["weight"],
            "types": ", ".join([t["type"]["name"] for t in details["types"]]),
            "abilities": ", ".join([a["ability"]["name"] for a in details["abilities"]]),
            "moves": ", ".join([m["move"]["name"] for m in details["moves"][:5]]),
            "stats": ", ".join([f"{s['stat']['name']}={s['base_stat']}" for s in details["stats"]])
        })

    end=time.time()
    final_time=(end-start)/60
    logging.info(f"Total Pokemon fetched: {len(all_pokemon)} in time {final_time:.2f} min")

    df=pd.DataFrame(data)
    ingest_db(df,'pokemon_data',engine)# calling the function to enter data into database

''' calling the main function '''

if __name__=='__main__':
    work_db()