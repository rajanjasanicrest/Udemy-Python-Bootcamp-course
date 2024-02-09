import imaplib
import getpass

M = imaplib.IMAP4_SSL('imap.gmail.com')
user = input("Enter your email: ")
password = getpass.getpass("Enter your password: ")
M.login(user,password)
M.list()
M.select("inbox")
typ ,data = M.search(None,'SUBJECT "this is a test email for python"')