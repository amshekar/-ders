import os,glob, re, nltk
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
from cStringIO import StringIO
from pymongo import MongoClient
import profileRanker

import sys
reload(sys)
sys.setdefaultencoding('utf-8')
from nltk.corpus import stopwords
from nltk import sent_tokenize
from nltk import PorterStemmer
ps = PorterStemmer()

nltk.download("punkt")
client = MongoClient()
db = client.hackathon
all_resumes = []
skill_set_universal = []
skills_list = open("universal_skillset.txt",'r')
for skill in skills_list.readlines():
    skill = skill.replace('\n', '')
    skill_set_universal.append(skill.lower())

skill_set_universal = set(skill_set_universal)

def pdf_to_sentences(filename):
    rsrcmgr = PDFResourceManager()
    retstr = StringIO()
    codec = 'utf-8'
    laparams = LAParams()
    device = TextConverter(rsrcmgr, retstr, codec=codec, laparams=laparams)
    fp = file(filename, 'rb')
    interpreter = PDFPageInterpreter(rsrcmgr, device)
    password = ""
    maxpages = 0
    caching = True
    pagenos = set()
    for page in PDFPage.get_pages(fp, pagenos, maxpages=maxpages, password=password, caching=caching,
                                  check_extractable=True):
        interpreter.process_page(page)
    text = retstr.getvalue()
    fp.close()
    device.close()
    retstr.close()
    return sent_tokenize(text)

def pdf_to_text(filename):
    rsrcmgr = PDFResourceManager()
    retstr = StringIO()
    codec = 'utf-8'
    laparams = LAParams()
    device = TextConverter(rsrcmgr, retstr, codec=codec, laparams=laparams)
    fp = file(filename, 'rb')
    interpreter = PDFPageInterpreter(rsrcmgr, device)
    password = ""
    maxpages = 0
    caching = True
    pagenos = set()
    for page in PDFPage.get_pages(fp, pagenos, maxpages=maxpages, password=password, caching=caching, check_extractable=True):
        interpreter.process_page(page)
    text = retstr.getvalue()
    fp.close()
    device.close()
    retstr.close()
    words = text.split()
    stop_words = set(stopwords.words('english'))
    filtered_words = [word for word in words if word not in stop_words]
    return filtered_words

"""
def extract_text(directory_name):
    os.chdir(directory_name)
    for file in glob.glob("*.pdf"):
        rsrcmgr = PDFResourceManager()
        retstr = StringIO()
        codec = 'utf-8'
        laparams = LAParams()
        device = TextConverter(rsrcmgr, retstr, codec=codec, laparams=laparams)
        fp = file(file, 'rb')
        interpreter = PDFPageInterpreter(rsrcmgr, device)
        password = ""
        maxpages = 0
        caching = True
        pagenos = set()
        for page in PDFPage.get_pages(fp, pagenos, maxpages=maxpages, password=password, caching=caching, check_extractable=True):
            interpreter.process_page(page)
        text = retstr.getvalue()
        fp.close()
        device.close()
        retstr.close()
        #return text
        #text = textract.process(file, encoding='ascii')
        words = text.split()

        stop_words = set(stopwords.words('english'))
        filtered_words = [word for word in words if word not in stop_words]
        all_resumes.append(filtered_words)

"""

def extract_email(resume):
    email = ""
    for token in resume:
        match = re.findall(r'[\w\.-]+@[\w\.-]+', token)
        if match :
            email = token
            break
    return email

def extract_phone(resume):
    token = ' '.join(resume)
    regex = re.compile("\+?\d[\( -]?\d{3}[\) -]?\d{3}[ -]?\d{2}[ -]?\d{2}")
    return re.findall(regex, token)

def extract_links(resume):
    link = re.findall(r'(https?://[^\s]+)', ' '.join(resume))
    return set(link)

def extract_skills(resume):
    skills = []
    for elem in enumerate(skill_set_universal):
        if any(item.lower() == elem[1].lower() for item in resume):
            skills.append(elem[1])
    return set(skills)

def extract_experience(sentences):
    stem_exp = ps.stem('experience')
    found_exps = []
    for sent in sentences:
        if stem_exp in sent:
            found_exps.append(sent)
    for exp in found_exps:
        expr = re.findall('\d+', exp)
    for exprs in expr:
        expers = exprs if exprs < 35 else 0
        break
    return expers

output = []
def process_resume(resume, candidate_name, file_path, sentences):
    email = extract_email(resume)
    skills = extract_skills(resume)
    phone = extract_phone(resume)
    links = extract_links(resume)
    experience = extract_experience(sentences)
    email = email.split('.com', 1)[0]
    file = open(file_path+ "/" +email + ".txt_"+ candidate_name, "w")
    #file.write(candidate_name)
    #file.write(experience)
    for i in skills:
        file.write(i + " ")
    file.close()
    for link in links:
        gitlink = link if "github" in link else ""
    pr = profileRanker(gitlink)
    output.append({"name":candidate_name,"email": email, "skills": skills, "phone": phone, "links": links, "gitHubRanking": pr.get_score(),"experience": experience})

    db.ResumeData.insert_one(output)
    return output