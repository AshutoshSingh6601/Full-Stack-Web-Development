from email import message
import smtplib
import getpass
email = input("Enter your email: ")
password = getpass.getpass(prompt="Enter your Password: ")
sender_email = "as0326142@gamil.com"
receiver_mail = "saifsayyed5624@gmail.com"
message = "Kysa Hai "
try:
    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtpobj:
        smtpobj.login(email, password)
        smtpobj.sendmail(sender_email,receiver_mail,message)
        print("email sent")

except Exception:
    print("Kuch to galat hai")