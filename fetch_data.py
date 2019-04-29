import csv
import pyodbc


# conn = pyodbc.connect('Driver={SQL Server};'
#                       'Server=CNCTWHXSQ0001.centene.com;'
#                       'Database=SFTNECM002;'
#                       'Trusted_Connection=yes;')

def get_extension():
    conn = db_connect('CNCTWHXSQ0001.centene.com', 'SFTNECM002')
    cursor = conn.cursor()

    cursor.execute("SELECT count(*) FROM extension_core")
    count = cursor.fetchone()[0]
    batch_size = 1000000
    print("total records in table are %s" % str(count))
    for offset in xrange(0, count, batch_size):
        cursor.execute("SELECT * FROM extension_core LIMIT %s OFFSET %s", (batch_size, offset))
        rows = cursor.fetchall()
        write_file("extension_core{id}.csv".format(id=offset), rows)


def get_second_query():
    conn = db_connect('CNCTWHXSQ0001.centene.com', 'SFTNECM002')
    cursor = conn.cursor()

    cursor.execute("SELECT count(*) FROM extension_core")
    count = cursor.fetchone()[0]
    batch_size = 1000000
    print("total records in table are %s" % str(count))
    for offset in xrange(0, count, batch_size):
        cursor.execute("SELECT * FROM extension_core LIMIT %s OFFSET %s", (batch_size, offset))
        rows = cursor.fetchall()
        write_file("extension_core{id}.csv".format(id=offset), rows)


def get_third_query():
    conn = db_connect('CNCTWHXSQ0001.centene.com', 'SFTNECM002')
    cursor = conn.cursor()

    cursor.execute("SELECT count(*) FROM extension_core")
    count = cursor.fetchone()[0]
    batch_size = 1000000
    print("total records in table are %s" % str(count))
    for offset in xrange(0, count, batch_size):
        cursor.execute("SELECT * FROM extension_core LIMIT %s OFFSET %s", (batch_size, offset))
        rows = cursor.fetchall()
        write_file("extension_core{id}.csv".format(id=offset), rows)


def get_forth_query():
    conn = db_connect('CNCTWHXSQ0001.centene.com', 'SFTNECM002')
    cursor = conn.cursor()

    cursor.execute("SELECT count(*) FROM extension_core")
    count = cursor.fetchone()[0]
    batch_size = 1000000
    print("total records in table are %s" % str(count))
    for offset in xrange(0, count, batch_size):
        cursor.execute("SELECT * FROM extension_core LIMIT %s OFFSET %s", (batch_size, offset))
        rows = cursor.fetchall()
        write_file("extension_core{id}.csv".format(id=offset), rows)


def get_fifth_query():
    conn = db_connect('CNCTWHXSQ0001.centene.com', 'SFTNECM002')
    cursor = conn.cursor()

    cursor.execute("SELECT count(*) FROM extension_core")
    count = cursor.fetchone()[0]
    batch_size = 1000000
    print("total records in table are %s" % str(count))
    for offset in xrange(0, count, batch_size):
        cursor.execute("SELECT * FROM extension_core LIMIT %s OFFSET %s", (batch_size, offset))
        rows = cursor.fetchall()
        write_file("extension_core{id}.csv".format(id=offset), rows)


def get_sixth_query():
    conn = db_connect('CNCTWHXSQ0001.centene.com', 'SFTNECM002')
    cursor = conn.cursor()

    cursor.execute("SELECT count(*) FROM extension_core")
    count = cursor.fetchone()[0]
    batch_size = 1000000
    print("total records in table are %s" % str(count))
    for offset in xrange(0, count, batch_size):
        cursor.execute("SELECT * FROM extension_core LIMIT %s OFFSET %s", (batch_size, offset))
        rows = cursor.fetchall()
        write_file("extension_core{id}.csv".format(id=offset), rows)


def write_file(file_name, rows):
    result_file = open(file_name, 'w')
    wr = csv.writer(result_file, dialect='excel')
    wr.writerows(rows)
    result_file.close()


def db_connect(server, database):
    con_string = 'Driver={ODBC Driver 17 for SQL Server};Server=%s;Database=%s;Trusted_Connection=yes;' % (server, database)
    # con_string = 'DSN=%s;UID=%s;PWD=%s;DATABASE=%s;' % (dsn, user, password, database)
    conn = pyodbc.connect(con_string)
    return conn


def main():
    print("python main function")
    get_extension()
    get_second_query()
    get_third_query()
    get_forth_query()
    get_fifth_query()
    get_sixth_query()


if __name__ == '__main__':
    main()
