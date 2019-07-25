import psycopg2

DB_FILE = 'backup.sql'

DB_NAME = 'rabotyNET'
DB_USER = 'postgres'
DB_PASS = 'postgres'
DB_HOST = 'localhost'
# table_list = ['users', 'company', 'user_role', 'verificationtoken']
# table_list = ['vacancy_resume']


def backup_table(table):
    with psycopg2.connect(dbname=DB_NAME, user=DB_USER,
                          password=DB_PASS, host=DB_HOST) as conn:
        cur = conn.cursor()
        cur.execute('SELECT * FROM {}'.format(table))
        back_up = open(DB_FILE, 'a')
        for row in cur:
            back_up.write('INSERT INTO {} VALUES {};\n'.format(table, str(row)))
        back_up.close()


def backup_all():
    for table in table_list:
        backup_table('public.' + table)


def clear_table(table):
    with psycopg2.connect(dbname=DB_NAME, user=DB_USER,
                          password=DB_PASS, host=DB_HOST) as conn:
        cur = conn.cursor()
        cur.execute('TRUNCATE {} CASCADE'.format('public.' + table))


def clear_all_table():
    for table in table_list:
        clear_table(table)


# clear_table('users')

def restore_db():
    with psycopg2.connect(dbname=DB_NAME, user=DB_USER,
                          password=DB_PASS, host=DB_HOST) as conn:
        cur = conn.cursor()
        back_up = open(DB_FILE, 'r')
        for line in back_up.readlines():
            # print(line)
            cur.execute(line)


def prepare_database():
    clear_all_table()
    restore_db()


