import os
from PyPDF2 import PdfMerger

# Percorsi delle cartelle
input_folder = "toMerge"
output_folder = "merged"
output_file = "blank.pdf"

# Crea la cartella result se non esiste
os.makedirs(output_folder, exist_ok=True)

# Inizializza il merger
merger = PdfMerger()

# Prende tutti i file PDF e li ordina alfabeticamente
pdf_files = [f for f in os.listdir(input_folder)
    if f.lower().endswith(".pdf")]

print(pdf_files)
print("These are the pdfs that will be merged.")
output_file = input("What should be the <name> of the result? ")

if not output_file.endswith(".pdf"):
    output_file += ".pdf"

# Aggiunge i PDF al merger
for pdf in pdf_files:
    pdf_path = os.path.join(input_folder, pdf)
    merger.append(pdf_path)

# Scrive il PDF finale
output_path = os.path.join(output_folder, output_file)
merger.write(output_path)
merger.close()

print(f"Merged PDF created in: {output_path}")
