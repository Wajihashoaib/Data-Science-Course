
import pandas as pd
import json

def txt_json(mul_files , jsonfile):
  with open("output_file.txt", "w" , newline = '') as outfile:
    for filename in mul_files:
      with open(filename) as infile:
        contents = infile.read()
        outfile.write(contents)
  file = open("output_file.txt","r")
  data = file.read()
  words = data.split()
  list =[]
  for word in words:
    if word[0] == '1':
      list.append(word)
      createjsonfile = open(jsonfile , 'w')
      json.dump(list, createjsonfile , indent = 6)

mul_files = ['file1.txt','file2.txt','file3.txt']
jsonfile = 'Json_file.json'

txt_json(mul_files , jsonfile)


