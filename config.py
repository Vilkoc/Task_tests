from base64 import b64decode as decode


TIMEOUT = 20
WEBDRIVER = 'Chrome'
URL = 'http://localhost:4200'


PAUSE = 2
EXTRA_LONG_PAUSE = 120

EMAIL = "rabotynet.test@gmail.com"
FROM_PWD = decode(b'cm9tYV9leHBlcnQ=').decode()
SMTP_SERVER = "imap.gmail.com"

DB_FILE = 'backup.sql'
DB_NAME = 'rabotyNET'
DB_USER = 'postgres'
DB_PASS = 'postgres'
DB_HOST = 'localhost'

EMAIL_SUBJECT_SIGNUP = "Registration on website RabotyNet"
USERNAME_SIGNUP = 'rabotynet.test@gmail.com'
PASSWORD = 'Qdrwbj!23'
PASSWORD_INCORRECT = 'vdeytvdv'

EMAIL_SUBJECT = 'Restore password on website RabotyNet'
USERNAME_PASSW_RECOVERY = 'rabotynet.test@gmail.com'
OLD_PASSWORD = 'Qdrwbj!23'
NEW_PASSWORD = 'Qdrwbj1@3'
