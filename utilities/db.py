import psycopg2
from config import DB_FILE, DB_NAME, DB_USER, DB_PASS, DB_HOST

<<<<<<< HEAD
def prepare_db():
    table_list = ['users', 'contact', 'address', 'claim', 'company', 'education', 'job',
  'pdf_resume', 'person', 'photo', 'requirement', 'resume', 'roles',
  'skill', 'user_role', 'vacancy', 'vacancy_resume',
  'verificationtoken']
=======

def prepare_db():
    table_list = ['users', 'contact', 'address', 'claim', 'company', 'education', 'job',
                  'pdf_resume', 'person', 'photo', 'requirement', 'resume', 'roles',
                  'skill', 'user_role', 'vacancy', 'vacancy_resume',
                  'verificationtoken']
>>>>>>> Nazar
    with psycopg2.connect(dbname=DB_NAME, user=DB_USER,
                          password=DB_PASS, host=DB_HOST) as conn:
        cur = conn.cursor()
        for table in table_list:
            cur.execute('TRUNCATE {} CASCADE'.format('public.' + table))

        back_up = open(DB_FILE, 'r')
        for line in back_up.readlines():
<<<<<<< HEAD
                cur.execute(line)

        back_up.close()
=======
            cur.execute(line)

        back_up.close()
>>>>>>> Nazar
