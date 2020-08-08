import psycopg2


def insert(CustomerName, CustomerFamily, NationalCode):
    try:
        connection = psycopg2.connect(
            user="postgres",
            password="sajad",
            host="localhost",
            port="5432",
            database="SajadDB"
        )

        cursor = connection.cursor()

        pg_insert = """ INSERT INTO public."Customer" (
                        "CustomerName", "CustomerFamily", "NationalCode")
                        VALUES (%s,%s,%s)"""

        inserted_values = (
            CustomerName,
            CustomerFamily,
            NationalCode,
        )

        cursor.execute(pg_insert, inserted_values)

        connection.commit()

        count = cursor.rowcount
        print("Successfully inserted", count, "records.")

    except(Exception, psycopg2.Error) as error:
        print("Error connecting to PostgreSQL database", error)
        connection = None

    finally:
        if (connection):
            cursor.close()
            connection.close()
            print("The PostgreSQL connection is now closed")
