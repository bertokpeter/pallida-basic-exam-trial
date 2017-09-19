# Create a function that takes email address as input in the following format:
# firstName.lastName@exam.com
# and returns a string that represents the user name in the following format:
# last_name first_name
# example: "elek.viz@exam.com" for this input the output should be: "Viz Elek"
# accents does not matter
email_address = input("Please enter your email address here (e.g elek.viz@exam.com): ")
def name_from_email(email_address):
    if not "@exam.com" in email_address:
        return "Your email address is not correct"
    else:
        dot = email_address.find(".")
        at = email_address.find("@")
        first_name = "" + email_address[:dot]
        last_name = "" + email_address[dot + 1:at]
        user_name = "" + capitalizer(last_name) + " " + capitalizer(first_name)
        return user_name
def capitalizer(name):
    name = name.capitalize()
    return name
print(name_from_email(email_address))