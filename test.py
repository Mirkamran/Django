import requests
import time
import httpx
import asyncio

#Below are static values
api_values = ["trivia", "math", "date"]

# start_time = time.time()

# def collect_data():
#     responses = []
#     start_time = time.time()
#     with httpx.Client() as client:
#         for i in range(1, 1000):
#             # Fetch data from the Numbers API
#             response = client.get(f'http://numbersapi.com/{i + 1}/math')
#             # Store the response text (or you  can use response.json() if the response is in JSON format)
#
#     end_time = time.time()
#     print(start_time - time.time())
#
# collect_data()
#

import httpx
import asyncio
import time

# Set the limit for concurrent requests
SEM_LIMIT = 10

async def fetch(client, number, semaphore):
    url = f'http://numbersapi.com/{number}/math'
    async with semaphore:  # Ensures the limit of concurrent tasks is respected
        response = await client.get(url)
        return response.text

async def main():
    semaphore = asyncio.Semaphore(SEM_LIMIT)  # Restrict the number of concurrent requests
    async with httpx.AsyncClient() as client:
        tasks = []
        for number in range(1, 1000):
            tasks.append(fetch(client, number + 1, semaphore))  # Use the semaphore for each request
        responses = await asyncio.gather(*tasks)

asyncio.run(main())
