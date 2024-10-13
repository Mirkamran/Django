import requests
import sqlite3
import time

#Below are static values
a = 100
api_values = ["trivia", "math", "date"]


def collect_data(input_data):
    responses = []
    for i in range(a):
        # Fetch data from the Numbers API
        response = requests.get(f'http://numbersapi.com/{i + 1}/{input_data}')
        # Store the response text (or you can use response.json() if the response is in JSON format)
        responses.append(response.text)
    return responses




# Step 1: Connect to the database (or create it)
conn = sqlite3.connect('numbersapi.db')

# Step 2: Create a cursor object
cursor = conn.cursor()

# Step 3: Define the SQL query for inserting data (ID is auto-incremented)
# insert_query = """
# INSERT INTO my_table (Type, Value)
# VALUES (?, ?);
# """
#
# for element in api_values:
#     data = collect_data(element)
#     for index, response in enumerate(data):
#         data_to_insert = [element, response]
#         print(data_to_insert)
#         cursor.execute(insert_query, data_to_insert)

for each_element in api_values:
    select_query = f"SELECT * FROM my_table WHERE Type = '{each_element}';"
    cursor.execute(select_query)

    # Step 4: Fetch all results
    rows = cursor.fetchall()

    # Step 5: Compare entries in  the table with ad-hoc requests
    count = 1

    for row in rows:
        zapros = requests.get(f'http://numbersapi.com/{count}/{each_element}')
        if row[2] == zapros.text:
            print(f"Values are equal for the number {count}")
        else:
            print(f"Not equal for {count}")
            count = count + 1


#Save data
#conn.commit()

#Close connection
conn.close()