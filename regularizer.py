import os
import unicodedata

def processer(fileName:str,divider:str):
    dictionary = {}
    with open(fileName,'r') as archive:
        lines = archive.readlines()

    i = 0
    while i < len(lines):
        line = lines[i].strip()
        if line.startswith("Archivo:"):
            key = line.split(":")[1].strip()
            dictionary[key] = []

        elif key is not None and not lines[i].startswith(divider) and not lines[i].startswith('Contenido:'):
            parragraph = lines[i].strip()
            if(parragraph and parragraph != divider):
                dictionary[key].append(parragraph)

        i+=1
    
    return dictionary

def stringRegularizer(wordList:list):
    regularized = []
    for string in wordList:
        string = unicodedata.normalize('NFKD',string).encode('ASCII','ignore').decode('utf-8')
        string = string.lower().strip()
        string = string.title()

        regularized.append(string)
    
    regularizedSet = set(regularized)

    return list(regularizedSet)

def dictionaryCleaner(dictionary:dict):
    for key in dictionary:
        value = dictionary[key]
        new_value = stringRegularizer(wordList=value)
        dictionary[key] = new_value
    
    return dictionary

def saveDictionaryToFile(dictionary:dict, file_name:str):
    with open(file_name, 'w') as file:
        for key, values in dictionary.items():
            file.write(f"Archivo:{key}\n")
            file.write(f"Contenido:\n\n")
            
            for value in values:
                file.write(f"{value}\n")
            file.write("\n")

file_name ="resultadoCrudo.txt"
divider = '-----------------------------'

dictionary = processer(fileName=file_name,divider=divider) 
dictionary = dictionaryCleaner(dictionary=dictionary)

for key in dictionary:
    print(f'(key: {key}, value: [{dictionary[key][:1]},...])\n') 


output_file_name = "resultadoProcesado.txt"
saveDictionaryToFile(dictionary, output_file_name)
