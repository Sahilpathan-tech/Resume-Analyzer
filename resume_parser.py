import PyPDF2
import docx

# Function to extract text from PDF
def extract_text_from_pdf(pdf_path):
    text = ""
    with open(pdf_path, "rb") as file:
        reader = PyPDF2.PdfReader(file)
        for page in reader.pages:
            if page.extract_text():
                text += page.extract_text() + "\n"
    return text

# Function to extract text from DOCX
def extract_text_from_docx(docx_path):
    doc = docx.Document(docx_path)
    text = "\n".join([para.text for para in doc.paragraphs])
    return text

# Function to analyze resume and score it based on keywords
def analyze_resume(resume_text):
    required_skills = ["Python", "SQL", "Machine Learning", "Data Science", "API", "Git", "AWS", "Django", "Flask"]
    
    score = 0
    for skill in required_skills:
        if skill.lower() in resume_text.lower():
            score += 10  # Each matching skill adds 10 points

    return score

# Change this to your actual resume file
resume_file = r"C:\New folder (3)\Resume_Analyzer\example_resume.pdf"

# Extract text based on file type
if resume_file.endswith(".pdf"):
    resume_text = extract_text_from_pdf(resume_file)
elif resume_file.endswith(".docx"):
    resume_text = extract_text_from_docx(resume_file)
else:
    print("Unsupported file format.")
    exit()

# Score the resume
resume_score = analyze_resume(resume_text)

# Print the results
print("\n📄 Resume Text Extracted:\n")
print(resume_text[:500])  # Print first 500 characters for preview
print("\n✅ Resume Score:", resume_score, "/ 100")