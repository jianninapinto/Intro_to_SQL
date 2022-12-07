import sqlite3
import pandas as pd

# SQLite connection

conn = sqlite3.connect('buddymove_holidayiq.sqlite3')
curs = conn.cursor()

# load in the CSV to a Pandas DataFrame
df = pd.read_csv('buddymove_holidayiq.csv')


if __name__ == '__main__':
    # Convert the DataFrame into a table called "review"
    df.to_sql('review', conn, if_exists='replace')

    # Query the table to ensure the data was added
    curs.execute('''
                SELECT *
                FROM review;
                ''')
    # print(curs.fetchall())

    # Number of rows
    curs.execute('''
                SELECT COUNT(*)
                FROM review;
                ''')
    # print(curs.fetchall())

    # Number of users Nature and Shopping reviews >= 100
    curs.execute('''
                SELECT COUNT(*)
                FROM review
                WHERE Nature >= 100
                AND Shopping >= 100;
                ''')
    # print(curs.fetchall())

    # Average Number of Review per Category
    curs.execute('''
    SELECT
        AVG(Sports),
        AVG(Religious),
        AVG(Nature),
        AVG(Theatre),
        AVG(Shopping),
        AVG(Picnic)
    FROM review;
    ''')
    print(curs.fetchall())
