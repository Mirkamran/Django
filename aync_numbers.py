import httpx
import asyncio
import sqlite3

# Set the limit for concurrent requests
SEM_LIMIT = 10

async def fetch(client, number, semaphore, api_value):
    url = f'http://numbersapi.com/{number}/{api_value}'
    async with semaphore:  # Ensures the limit of concurrent tasks is respected
        response = await client.get(url)
        return response.text


async def main(api_value):
    semaphore = asyncio.Semaphore(SEM_LIMIT)  # Restrict the number of concurrent requests
    async with httpx.AsyncClient() as client:
        tasks = []
        for number in range(0, 3000):
            tasks.append(fetch(client, number + 1, semaphore, api_value))  # Use the semaphore for each request
        responses = await asyncio.gather(*tasks)
        return responses



# Step 1: Connect to the database (or create it)
conn = sqlite3.connect('numbersapi.db')

# Step 2: Create a cursor object
cursor = conn.cursor()

# Step 3: Define the SQL query for inserting data (ID is auto-incremented)
insert_query = """
INSERT INTO my_table (Type, Value)
VALUES (?, ?);
"""
math_api_value = "date"

for element in asyncio.run(main(math_api_value)):
    data_to_insert = [math_api_value, element]
    cursor.execute(insert_query, data_to_insert)



#Save data
conn.commit()

#Close connection
conn.close()