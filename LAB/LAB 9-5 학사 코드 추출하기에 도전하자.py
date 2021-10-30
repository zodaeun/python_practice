import re

text = '''101 Com PythonProgramming
102 Mat LinearAlgebra
103 ENG ComputerEnglish'''

pText = re.findall('[0-9]+', text)
print(pText)
