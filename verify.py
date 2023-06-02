
import phonenumbers
import requests
import smtplib
import dns.resolver

def verify_phone(phone_num: str) -> bool:

    """
    Takes a phone number formatted into a string as input and returns a boolean value if said number exists.
    """

    try:

        parsed_num = phonenumbers.parse(phone_num, None)
        return phonenumbers.is_valid_number(parsed_num)
    
    except phonenumbers.phonenumberutil.NumberParseException:

        return False

def verify_email(email: str) -> bool:

    """
    Takes an email formatted into a string as input and returns a boolean value if said email exists.
    """

    username, domain = email.split('@')

    try:

        mx_records = dns.resolver.resolve(domain, 'MX')
        mx_record = str(mx_records[0].exchange)
    
    except dns.resolver.NoAnswer:

        return False
    
    try:

        smtp_server = smtplib.SMTP(mx_record)
        smtp_server.helo(smtp_server.local_hostname)

        code, message = smtp_server.verify(email)

        smtp_server.quit()

        return True
    
    except smtplib.SMTPException:

        return False

def verify_url(url: str) -> bool:

    """
    Takes a URL formatted into a string as input and returns a boolean value if said URL exists.
    """

    try:

        response = requests.head(url)
        return True
    
    except requests.exceptions.RequestException: 

        return False
