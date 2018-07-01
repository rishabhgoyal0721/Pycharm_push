import smtplib
from string import Template
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

MY_ADDRESS = 'RISHABH.GOYAL@GMAIL.COM'
PASSWORD = 'bacsded'

def get_contacts(fielname):

	names = []
	email = []
	with open(filename, mode ='r', encoding = 'utf-8') as contacts_file:
		for a_contact in contacts_file:
			names.append(a_contact.split()[0])
			email.append(a_contact.split()[10])
		return (names, email)
		
def read_template(filename):
	with open(filename, mode= 'r', emncoding ='utf-8') as template_file:
		template_file_content = template_file.read()
		return(Template(template_file_content))

def main():
	emails,names = get_contacts('my_contacts.txt')
	message_template = read_template('message.txt')

	s= smtplib.SMTP(host = 'WWW.GMAIL.COM' , port ='587')
	s.starttls()
	s.login(MY_ADDRESS, PASSWORD)

	for name, email in zip(names, emails):
		msg = MIMEMultipart()
		message = message_template.substitute(PERSON_NAME=name.title())
	    print(message)
        msg['From']=MY_ADDRESS
        msg['To']=email
        msg['Subject']="This is TEST"
        
        
        msg.attach(MIMEText(message, 'plain'))
        s.send_message(msg)
        del (msg)
        
    # Terminate the SMTP session and close the connection
    s.quit()
    
if __name__ == '__main__':
    main()
				