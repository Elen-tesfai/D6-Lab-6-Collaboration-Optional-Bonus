# -*- coding: utf-8 -*-
# convert_encoding.py - Convert file encoding from UTF-16 to UTF-8

# Open the file in UTF-16 LE encoding (with BOM)
with open('app.py1', 'r', encoding='utf-16') as file:
    content = file.read()

# Save the content back to the file in UTF-8 encoding, without BOM
with open('app.py1', 'w', encoding='utf-8') as file:
    file.write(content)

print('File encoding has been successfully converted to UTF-8.')