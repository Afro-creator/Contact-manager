def is_valid_email(email):
    import re
    email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return re.match(email_regex, email) is not None

def is_valid_phone(phone):
    return phone.isdigit() and len(phone) in [10, 11]  # Assuming 10 or 11 digit phone numbers

def validate_contact(name, email, phone):
    if not name:
        return False, "Name cannot be empty."
    if not is_valid_email(email):
        return False, "Invalid email format."
    if not is_valid_phone(phone):
        return False, "Phone number must be 10 or 11 digits."
    return True, "Contact is valid."