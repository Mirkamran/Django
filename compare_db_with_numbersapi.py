import sqlite3
import httpx
import asyncio


async def fetch_data(client, count, each_element):
    url = f'http://numbersapi.com/{count}/{each_element}'
    response = await client.get(url)
    return response.text


async def main():
    conn = sqlite3.connect('numbersapi.db')
    cursor = conn.cursor()

    api_values = ["trivia", "math", "date"]

    async with httpx.AsyncClient() as client:
        for each_element in api_values:
            select_query = f"SELECT * FROM my_table WHERE type = '{each_element}';"
            cursor.execute(select_query)

            # Fetch all results, including the row ID
            rows = cursor.fetchall()

            count = 1

            # Compare entries in the table with ad-hoc requests
            for row in rows:
                row_id = row[0]  # Assuming the first column is the ID
                zapros_text = await fetch_data(client, count, each_element)

                if row[2] == zapros_text:  # row[2] corresponds to 'value'
                    print(f"Values are equal for the number {count}")
                else:
                    print(f"Not equal for {count}")

                    # Update the current value in the table using the row's unique ID
                    update_query = """
                    UPDATE my_table
                    SET value = ?
                    WHERE ID = ?;
                    """
                    cursor.execute(update_query, (zapros_text, row_id))
                    print(f"Updated value for number {count}, row ID {row_id}")

                count += 1

    # Save changes
    conn.commit()

    # Close connection
    conn.close()


# Run the async main function
asyncio.run(main())
