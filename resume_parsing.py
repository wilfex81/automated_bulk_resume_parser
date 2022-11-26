import spacy
import pdfminer
import re
import os
import pandas as pd

import pdf2txt

def convert_pdf(f):
    """Convert pdf to txt"""
    output_filename = os.path.basename(os.path.splitext(f)[0] + '.txt')
    output_filepath = os.path.join('output/txt/', output_filename)
    pdf2txt.main(args=[f, "--outfile", output_filepath])#converts pdf to txt and saves in the given location

    print(output_filepath + " saved succesfully!!!")
    return open(output_filepath).read()

os.path.splitext("wilfex_kipchirchir_cv")[0]

#loads the language model
nlp = spacy.load('en-core-web-sm')

result_dict = {"name": [], "phone": [],"email": [], "skills": []}

names = []
phones = []
emails = []
skills = []

def parse_content(text):
    skillset = re.compile('python|java|sql|hadoop|tableau')
    phone_num = re.compile('(\d{3}[-\.\s]??\d{3}[-\.\s]??\d{4}|\(\d{3}\)\s*\d{3}[-\.\s]??\d{4}|\d{3}[-\.\s]??\d{4})')
    doc = nlp(text)
    name = [entity.text for entity in doc.ents if entity.label_ is 'PERSON'][0]
    print(name)
    email = [word for word in doc if word.like_email == True][0]
    print(email)
    phone = str(re.findall(phone_num,text.lower()))
    skills_list = re.findall(skillset,text.lower())
    unique_skills_list = str(set(skills_list))
    names.append(name)
    emails.append(email)
    phones.append(phone)
    skills.append(unique_skills_list)
    print("Extraction completed successfully!!!")

for file in os.listdir('resumes/'):
    if file.endswith('.pdf'):
        print("Reading....." + file)
        txt = convert_pdf(os.path.join('resumes/', file))
        parse_content(txt)

result_dict['name'] = names
result_dict['phone'] = phones
result_dict['email'] = emails
result_dict['skills'] = skills

print(result_dict)

result_df = pd.DataFrame[result_dict]
print(result_df)






