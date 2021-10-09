# Q24 Remove all the special characters and numbers from the following string
#Text = '%p34@y!*-*!t68h#&on404'

text = '%p34@y!*-*!t68h#&on404'
new_text=""
for character in text:
    if character.isalpha():
        new_text+=character

print(new_text)