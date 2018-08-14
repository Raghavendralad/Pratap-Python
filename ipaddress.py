import re

pattern = re.compile(r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})\s(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})')

with open('ip.txt', 'r') as f:
  contents = f.read()
  matches = pattern.finditer(contents)
  for match in matches:
   print(match.group(1))
