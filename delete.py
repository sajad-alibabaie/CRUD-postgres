import psycopg2


def delete(NationalCode):
    try:
        connection = psycopg2.connect(
            user="postgres",
            password="sajad",
            host="localhost",
            port="5432",
            database="SajadDB"
        )

        cursor = connection.cursor()

        pg_delete = """DELETE FROM public."Customer" where "NationalCode" = %s"""

        cursor.execute(pg_delete, (NationalCode,))
        connection.commit()
        count = cursor.rowcount
        print("Successfully deleted", count, "rows.")

    except(Exception, psycopg2.Error) as error:
        print("Error in Deleting the data:", error)
        connection = None

    finally:
        if connection != None:
            cursor.close()
            connection.close()
            print("PostgreSQL connection is now closed")
