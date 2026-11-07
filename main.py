import pymupdf ,json
from pathlib import Path


# path="data/raw"
def extract_pdf(path):
    doc=pymupdf.open(path)
    pages=[]
    for i,page in enumerate(doc):
        pages.append({
            "source":path.name,
            "page":i+1,
            "text":page.get_text()
        })
    return pages
extract_pdf(path='../data/raw/R22B.Tech.CSE(AIML)CourseStructureSyllabus2.pdf')
print("Hello")
