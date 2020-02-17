#!/usr/bin/python3
import re, pyperclip

#Regex for phone numbers
phoneRegex = re.compile(r'''
# 415-555-000, 555-0000, (451) 555-000, 555-0000 ext 12345, ext., x12345, x 12345
(
((\d\d\d) | (\(\d\d\d\)))?  # area code (optional)
(\s | - | .)                # first seperator
\d\d\d                      # first 3 digits
(- | .)                     # seperator
\d\d\d\d                    # last 4 digits
(((ext (\.)?\s) |x)         # extension word-part (optional)
    (\d{2:5}))?             #extension number-part optional
)
''', re.VERBOSE)

#Regex for email addresses
emailRegex = re.compile(r'''
#some.+_thing@some.+_thing.com

[a-zA-Z0-9_.+]+             # name part
@                           # @ symbol
[a-zA-Z0-9_.+]+             # domain name part

''', re.VERBOSE)

#Get the text off the clipboard
text = pyperclip.paste()

#Extract the email/phone number from this text
extractedPhone = phoneRegex.findall(text)
extractedEmail = emailRegex.findall(text)

allPhoneNumbers = []
for phoneNumber in extractedPhone:
    allPhoneNumbers.append(phoneNumber[0])

#Copy the extracted email/phone to the clipboard
results = '\n'.join(allPhoneNumbers) + '\n' + '\n'.join(extractedEmail)
pyperclip.copy(results)
