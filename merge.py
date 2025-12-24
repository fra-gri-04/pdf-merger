import os
from PyPDF2 import PdfMerger

# Folder's names and paths
input_folder = "in"
output_folder = "out"
output_file = "blank.pdf"

# Creates the output folder if it doesn't exist.
os.makedirs(output_folder, exist_ok=True)

# Merger initialization
merger = PdfMerger()

# Takes all the .pdf from the input folder
pdf_files = [f for f in os.listdir(input_folder)
    if f.lower().endswith(".pdf")]

print(pdf_files)
print("These are the pdfs that will be merged.")
output_file = input("What should be the <name> of the result? ")

if not output_file.endswith(".pdf"):
    output_file += ".pdf"

# Adds pdfs to merger
for pdf in pdf_files:
    pdf_path = os.path.join(input_folder, pdf)
    merger.append(pdf_path)

# Writes the resulting merged pdf
output_path = os.path.join(output_folder, output_file)
merger.write(output_path)
merger.close()

print(f"Merged PDF created in: {output_path}")
