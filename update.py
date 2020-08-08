import psycopg2

def update(NationalCode, CustomerName):
    try:
        connection = psycopg2.connect(
            user="postgres",
            password="sajad",
            host="localhost",
            port="5432",
            database="SajadDB"
        )

        cursor = connection.cursor()

        print("Customer table before updating")
        pg_select = """SELECT * FROM public."Customer" WHERE "NationalCode" = %s"""
        cursor.execute(pg_select, (NationalCode, ))
        customer_record = cursor.fetchone()
        print(customer_record)

        pg_update = """Update public."Customer" set "CustomerName" = %s WHERE "NationalCode" = %s"""
        cursor.execute(pg_update, (CustomerName, NationalCode))
        connection.commit()
        count = cursor.rowcount
        print(count, "Successfully Updated!")

        print("Customer table after updating")
        pg_select = """SELECT * FROM public."Customer" WHERE "NationalCode" = %s"""

        cursor.execute(pg_select, (NationalCode,))
        customer_record = cursor.fetchone()
        print(customer_record)

    except(Exception, psycopg2.Error) as error:
        print("Error in updating the data:", error)
        connection = None

    finally:
        if connection != None:
            cursor.close()
            connection.close()
            print("PostgreSQL connection is now closed")