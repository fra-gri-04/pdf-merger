## How to install requirements

The only external library you need is PyPDF2. At the time of the release of this script, its version is 3.0.1.

You can directly install it using

```
pip install PyPDF2
```

Or using the command

```
pip install -r requirements.txt
```

## How to use

To use this simple script all you need to do is place inside the `toMerge` folder the pdfs you want to merge.
The script will take all the .pdf files in alphabetical order and merge them into a single one.
The result will be added to the `merged` folder.
You can choose the name of the output.

If you have python installed, you can run the command:

```
python merge_pdf.py
```

If you are on windows and 

