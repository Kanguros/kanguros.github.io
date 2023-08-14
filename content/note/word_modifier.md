Title: Word file modifier
Date: 08.08.2023
Tags: python
Status: hidden


This Python script allows you to modify Word documents by performing specific actions on their content. The script uses the `python-docx` library to work with Word documents.

## Features

The script includes the following features:

1. Remove text enclosed in square brackets from paragraphs.
2. Correct the order of numeric values within paragraphs.
3. Set the font type of all text runs to a specified font.
4. Align formatting of numeric points within paragraphs.

## Prerequisites

Before using the script, make sure you have the following installed:

- Python (version 3.6 or higher)
- The `python-docx` library (install using `pip install python-docx`)

## Usage

1. Paste the code to the new file.
2. Open a terminal and navigate to the directory containing the script.
3. Run the script using the following command:

```bash
python script.py input_file.docx
```

## Code

```python
import sys
import logging
from docx import Document

logging.basicConfig(filename='script.log', level=logging.ERROR, format='%(asctime)s - %(levelname)s: %(message)s')

def remove_text_between_brackets(doc):
    """
    Remove text enclosed in square brackets from all paragraphs in the document.

    Args:
        doc (Document): The Word document to be modified.
    """
    try:
        for paragraph in doc.paragraphs:
            open_bracket = 0
            new_text = ''
            for char in paragraph.text:
                if char == '[':
                    open_bracket += 1
                elif char == ']':
                    open_bracket -= 1
                elif open_bracket == 0:
                    new_text += char
            paragraph.text = new_text
    except Exception as e:
        logging.error(f"Error in remove_text_between_brackets: {str(e)}")

def correct_numeric_order(doc):
    """
    Correct the order of numeric values in each paragraph by sorting them.

    Args:
        doc (Document): The Word document to be modified.
    """
    try:
        for paragraph in doc.paragraphs:
            words = paragraph.text.split()
            nums = [word for word in words if word.isdigit()]
            nums.sort(key=int)
            for i, word in enumerate(words):
                if word.isdigit():
                    words[i] = nums.pop(0)
            paragraph.text = ' '.join(words)
    except Exception as e:
        logging.error(f"Error in correct_numeric_order: {str(e)}")

def set_same_font_type(doc, font_type):
    """
    Set the font type of all text runs in the document to a specified font.

    Args:
        doc (Document): The Word document to be modified.
        font_type (str): The name of the font to be applied.
    """
    try:
        for paragraph in doc.paragraphs:
            for run in paragraph.runs:
                run.font.name = font_type
    except Exception as e:
        logging.error(f"Error in set_same_font_type: {str(e)}")

def align_numeric_points(doc):
    """
    Align formatting of numeric points in each paragraph.

    Args:
        doc (Document): The Word document to be modified.
    """
    try:
        for paragraph in doc.paragraphs:
            if paragraph.text.startswith('- '):
                paragraphs = paragraph.text.split('\n')
                new_paragraphs = []
                for p in paragraphs:
                    if p.startswith('- '):
                        new_paragraphs.append(p.replace('- ', '', 1))
                    else:
                        new_paragraphs.append(p)
                paragraph.clear_content()
                for p in new_paragraphs:
                    paragraph.add_run('- ' + p)
    except Exception as e:
        logging.error(f"Error in align_numeric_points: {str(e)}")

def main(input_file):
    """
    Main function to modify the Word document according to specified actions.

    Args:
        input_file (str): The path to the input Word document.
    """
    try:
        doc = Document(input_file)

        remove_text_between_brackets(doc)
        correct_numeric_order(doc)
        set_same_font_type(doc, 'Arial')
        align_numeric_points(doc)

        modified_file = 'modified_' + input_file
        doc.save(modified_file)
        print(f"Modified document saved as: {modified_file}")
    except Exception as e:
        logging.error(f"Error in main: {str(e)}")

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python script.py <input_file>")
    else:
        input_file = sys.argv[1]
        main(input_file)
```
