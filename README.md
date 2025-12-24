<small> English Version</small>
 
## How to install requirements

The only external library you need is PyPDF2. At the time of the release of this script, its version is 3.0.1.

You can directly install it using

```
pip install PyPDF2
```

Or, more generally, you can install the requirements of the project

```
pip install -r requirements.txt
```

## How to use the merger

To use this simple script all you need to do is place inside a `in` folder, in the same path of the script the pdfs, you want to merge.
The script will take all the .pdf files in alphabetical order and merge them into a single one.
The result will be added to the `out` folder.
You can choose the name of the output.

To execute, run the command:

```
python merge_pdf.py
```

---

<small> Versione Italiana</small>

## Come installare le dipendenze necessarie

L'unica libreria esterna da installare è PyPDF2. Al momento della pubblicazione di questo script, la sua versione è la 3.0.1.
Puoi installarla direttamente usando

```
pip install PyPDF2
```
Oppure in modo più generale, installando i requirements del progetto

```
pip install -r requirements.txt
```

## Come utilizzare il merger

Per usare questo semplice script ciò che devi fare è inserire i pdf da unire in una cartella `in` nello stesso path dello script.
Lo script raccoglierà i .pdf in ordine alfabetico e li unirà in un unico file risultante, inserito nella cartella `out`.
Potrai decidere il nome del pdf risultante.

Per eseguire lo script basterà eseguire

```
python merge_pdf.py
```

