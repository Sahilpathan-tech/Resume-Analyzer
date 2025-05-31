import tkinter as tk
from tkinter import filedialog, messagebox, ttk
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

# Function to analyze resume and score it
def analyze_resume(resume_text):
    required_skills = ["Python", "SQL", "Machine Learning", "Data Science", "API", "Git", "AWS", "Django", "Flask"]
    
    score = 0
    for skill in required_skills:
        if skill.lower() in resume_text.lower():
            score += 10  # Each matching skill adds 10 points

    return score

# Function to handle file selection and scoring
def upload_resume():
    file_path = filedialog.askopenfilename(filetypes=[("PDF files", ".pdf"), ("Word files", ".docx")])
    
    if not file_path:
        return

    try:
        if file_path.endswith(".pdf"):
            resume_text = extract_text_from_pdf(file_path)
        elif file_path.endswith(".docx"):
            resume_text = extract_text_from_docx(file_path)
        else:
            messagebox.showerror("Error", "Unsupported file format!")
            return

        resume_score = analyze_resume(resume_text)

        result_label.config(text=f"✅ Resume Score: {resume_score} / 100", fg="#4CAF50")
        text_box.delete("1.0", tk.END)
        text_box.insert(tk.END, resume_text[:1000])  # Show first 1000 characters

    except Exception as e:
        messagebox.showerror("Error", f"Something went wrong:\n{e}")

# Create GUI window
root = tk.Tk()
root.title("Resume Analyzer")
root.geometry("700x550")
root.configure(bg="#F5F5F5")

# Styling
title_label = tk.Label(root, text="📄 Resume Analyzer", font=("Arial", 18, "bold"), bg="#F5F5F5", fg="#333")
title_label.pack(pady=10)

upload_button = tk.Button(root, text="📂 Upload Resume", command=upload_resume, font=("Arial", 14), bg="#4CAF50", fg="white", padx=20, pady=5)
upload_button.pack(pady=10)

result_label = tk.Label(root, text="Upload a resume to analyze.", font=("Arial", 12), bg="#F5F5F5", fg="#555")
result_label.pack()

frame = tk.Frame(root, bg="white", bd=2, relief="sunken")
frame.pack(pady=10, padx=20, fill="both", expand=True)

text_box = tk.Text(frame, wrap="word", height=15, width=70, font=("Arial", 10), padx=10, pady=10, bg="white")
text_box.pack(expand=True, fill="both")

scrollbar = ttk.Scrollbar(frame, command=text_box.yview)
scrollbar.pack(side="right", fill="y")
text_box.config(yscrollcommand=scrollbar.set)

# Run the GUI
root.mainloop()