import requests
import os
import json
from dotenv import load_dotenv
import sqlite3

# Load environment file
load_dotenv('../allAPI.env')

def set_url():
    COUNTRY_POPULATION_API = os.getenv('COUNTRY_API')

    if not COUNTRY_POPULATION_API:
        print("Error: API URL not found in allAPI.env")
        exit()

    return COUNTRY_POPULATION_API

def create_table():
    conn = sqlite3.connect('population.db')
    cursor = conn.cursor()
    
    cursor.execute(""" 
    CREATE TABLE IF NOT EXISTS population(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    COUNTRY TEXT,
    CODE TEXT,
    iso3 TEXT,
    YEAR INTEGER,
    POPULATION INTEGER
    )""")
    
    conn.commit()
    conn.close()
    
def show_data(limit=10):
    conn = sqlite3.connect("population.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM population LIMIT ?", (limit,))
    rows = cursor.fetchall()

    for row in rows:
        print(row)

    conn.close()

    

def insert_data(data):
    conn = sqlite3.connect('population.db')
    cursor = conn.cursor()
    
    for country in data['data']:
        cname = country['country']
        code = country['code']
        iso3 = country['iso3']
        
        for record in country['populationCounts']:
            year = record['year']
            population_val = record['value']
            
            cursor.execute("""
            INSERT INTO population (COUNTRY,CODE,iso3,YEAR,POPULATION)
            VALUES(?,?,?,?,?)
            """,(cname,code,iso3,year,population_val))
            
    conn.commit()
    conn.close()
    
    print("Data inserted successfully.")
    
        
    
   
    

def select_country():
    while True:
        try:
            user_input_country = input("Enter a country name: ").strip()
            if not user_input_country:
                raise ValueError("Country name is required.")
            return user_input_country
        except ValueError as e:
            print(f"Error: {e}")

def select_year():
    while True:
        try:
            user_input_year = int(input("Enter a year: "))
            if not user_input_year:
                raise ValueError("Year is required.")
            return user_input_year
        except ValueError as e:
            print(f"Error: {e}")

def get_data(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print("Error fetching data")
        return None

# def get_population_by_year(data, country_name, year):
#     for country in data['data']:
#         if country['country'].lower() == country_name.lower():
#             for record in country['populationCounts']:
#                 if int(record['year']) == year:
#                     return record['value']
#             return f"Population data not found for year {year}"
#     return "Country not found"

def get_population_by_year(data, country_name, year):
    for country in data['data']:
        if country['country'].lower() == country_name.lower():
            code = country['code']
            iso3 = country['iso3']
            for record in country['populationCounts']:
                if int(record['year']) == year:
                    return record['value'], code, iso3
            return None, code, iso3   # year not found
    return None, None, None   # country not found


def main():
    url = set_url()
    data = get_data(url)

    if data is None:
        return
    
    create_table()
    insert_data(data)
    country_name = select_country()
    year = select_year()

    population,iso3,code = get_population_by_year(data, country_name, year)

    print(f"\nPopulation of {country_name} in {year}: {population}")
    print(f'Country Code: {code}')
    print(f'iso3 : {iso3}')
    print()
    print("In DataBase:")
    show_data(10)
if __name__ == "__main__":
    main()
