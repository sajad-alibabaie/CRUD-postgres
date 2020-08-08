import psycopg2


def select():
    try:
        connection = psycopg2.connect(
            user="postgres",
            password="sajad",
            host="localhost",
            port="5432",
            database="SajadDB"
        )

        cursor = connection.cursor()
        pg_select = """SELECT * FROM public."Customer" """
        cursor.execute(pg_select)

        print("Selected rows from book table")
        customer_records = cursor.fetchall()

        print("Records of books in the table")
        for row in customer_records:
            print("id = ", row[0])
            print("CustomerName = ", row[1])
            print("CustomerFamily  = ", row[2])
            print("NationalCode = ", row[3])
            print("---------------****---------------", "\n")

    except (Exception, psycopg2.Error) as error:
        print("Error selecting data from table book", error)
        connection = None

    finally:
        if (connection):
            cursor.close()
            connection.close()
            print("PostgreSQL connection is now closed")
