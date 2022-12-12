import psycopg2
from os import getenv
import pandas as pd

# PostgreSQL Connection Credentials

# "User & Default Database" from ElephantSQL
DBNAME = getenv('DBNAME')
USER = getenv('USER')
# "Password" from ElephantSQL
PASSWORD = getenv('PASSWORD')
# "Server" from ElephantSQL
HOST = getenv('HOST')

# Make Postgres Connection and Cursor
pg_conn = psycopg2.connect(dbname=DBNAME, user=USER,
                           password=PASSWORD, host=HOST)
pg_curs = pg_conn.cursor()


def execute_query_pg(curs, conn, query):
    results = curs.execute(query)
    conn.commit()
    return results


TITANIC_TABLE = '''
CREATE TABLE IF NOT EXISTS titanic_table(
    passenger_id SERIAL PRIMARY KEY,
    Survived INT NOT NULL,
    Pclass INT NOT NULL,
    Name VARCHAR(100) NOT NULL,
    Sex VARCHAR(10) NOT NULL,
    Age FLOAT NOT NULL,
    Siblings_Spouses_Aboard INT NOT NULL,
    Parents_Children_Aboard INT NOT NULL,
    Fare FLOAT NOT NULL
);
'''

DROP_TITANIC_TABLE = '''
DROP TABLE IF EXISTS titanic_table;
'''

df = pd.read_csv('titanic.csv')
# removing any single quotes in the Name column
df['Name'] = df['Name'].str.replace("'", '')

if __name__ == '__main__':

    # Create the table and its associated Schema
    # Drop Table
    execute_query_pg(pg_curs, pg_conn, DROP_TITANIC_TABLE)
    # Create Table
    execute_query_pg(pg_curs, pg_conn, TITANIC_TABLE)

    records = df.values.tolist()

    for record in records:
        insert_statement = '''
            INSERT INTO titanic_table (survived, pclass, name, sex, age, siblings_spouses_aboard, parents_children_aboard, fare)
            VALUES {};
            '''.format(tuple(record))
        execute_query_pg(pg_curs, pg_conn, insert_statement)
