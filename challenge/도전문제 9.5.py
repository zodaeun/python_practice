import re

text = '''101 COM PythonProgramming
102 MAT LinearAlgebra
103 ENG ComputerEnglish'''

pText1 = re.findall('[0-9][0-9][0-9]', text)
print(pText1)

pText2 = re.findall('[A-Z][A-Z][A-Z]',text)
print(pText2)

