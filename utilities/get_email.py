import imaplib
from time import sleep
from config import EMAIL, FROM_PWD, SMTP_SERVER


def get_link(subject):
    mail = imaplib.IMAP4_SSL(SMTP_SERVER)
    mail.login(EMAIL, FROM_PWD)
    mail.select('inbox')

    typ, data = mail.search(None, '(SUBJECT "%s")' % subject)
    if len(data) == 0:
        sleep(20)
        print('wait email')
        typ, data = mail.search(None, '(SUBJECT "%s")' % subject)

    mail_ids = data[0].split()[-1]

    typ, data = mail.fetch(mail_ids, '(RFC822)')

    str_link = data[0][1].decode("utf-8")
    link = str_link[str_link.find('link:') + 5: str_link.find('If you')]
    print(link)
    return link
