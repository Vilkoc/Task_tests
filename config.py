from base64 import b64decode as decode

TIMEOUT = 10

PAUSE = 2
EXTRA_LONG_PAUSE = 20

EMAIL_SIGNUP = "rabotynet.test@gmail.com"
FROM_SIGNUP = decode(b'cm9tYV9leHBlcnQ=').decode()

EMAIL_FORGOT_PASSWORD = "rabotynet.test.fp@gmail.com"
FROM_FORGOT_PASSWORD = decode(b'cm9tYV9leHBlcnQ=').decode()

SMTP_SERVER = "imap.gmail.com"

DB_FILE = 'backup.sql'
DB_NAME = 'rabotyNET'
DB_USER = 'postgres'
DB_PASS = 'root'
DB_HOST = 'localhost'

EMAIL_SUBJECT_SIGNUP = "Registration on website RabotyNet"
USERNAME_SIGNUP = 'rabotynet.test@gmail.com'
PASSWORD = 'Qdrwbj!23'
PASSWORD_INCORRECT = 'vdeytvdv'

EMAIL_SUBJECT_PASSW_RECOVERY = 'Restore password on website RabotyNet'
USERNAME_PASSW_RECOVERY = 'rabotynet.test@gmail.com'
OLD_PASSWORD = 'Qdrwbj!23'
NEW_PASSWORD = 'Qdrwbj1@3'
