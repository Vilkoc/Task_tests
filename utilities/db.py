import psycopg2
from config import DB_FILE, DB_NAME, DB_USER, DB_PASS, DB_HOST
import time
from config import TIMEOUT


def prepare_db():
    table_list = ['users', 'contact', 'address', 'claim', 'company', 'education', 'job',
                  'pdf_resume', 'person', 'photo', 'requirement', 'resume', 'roles',
                  'skill', 'user_role', 'vacancy', 'vacancy_resume',
                  'verificationtoken']

    with psycopg2.connect(dbname=DB_NAME, user=DB_USER,
                          password=DB_PASS, host=DB_HOST) as conn:
        cur = conn.cursor()
        for table in table_list:
            cur.execute('TRUNCATE {} CASCADE'.format('public.' + table))

        back_up = open(DB_FILE, 'r')
        for line in back_up.readlines():
            cur.execute(line)

        back_up.close()


def change_varification_link(user):
    with psycopg2.connect(dbname=DB_NAME, user=DB_USER,
                          password=DB_PASS, host=DB_HOST) as conn:
        cur = conn.cursor()
        cur.execute("UPDATE public.verificationtoken SET token='3e83667c-c59c-4fda-aa7a-a47346a3cd6a' WHERE user_id=\
          (SELECT user_id FROM public.users WHERE login='{}');".format(user))


def wait_user_update(user, timeout=TIMEOUT):
    """ Wait while user will be registered in db """
    end = time.time() + timeout
    with psycopg2.connect(dbname=DB_NAME, user=DB_USER,
                          password=DB_PASS, host=DB_HOST) as conn:
        cur = conn.cursor()

        while time.time() < end:
            cur.execute("SELECT users.enabled FROM public.users WHERE user_id=\
              (SELECT user_id FROM public.users WHERE login='{}');".format(user))
            result = cur.fetchone()[0]
            if result == True:
                return
    raise Exception("No enougth elements")
