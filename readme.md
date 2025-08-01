````markdown
# PDF Word Substituter

A Python script that uses **PyMuPDF (fitz)** to find and replace words in PDF files. It preserves font styles (when possible) and allows precise positioning of the replacement text.

---

## 🌐 Repository
**GitHub Repository:** [pdf-word-substituter](https://github.com/Nahuelseoane/pdf-word-substituter)

---

## ✨ Features
- Replace specific words or phrases in a PDF.
- Preserve original font and size (fallback to Helvetica if unavailable).
- Adjust text positioning with `x_offset` and `y_offset`.
- Automatically save the modified PDF without altering the original.

---

## 🛠️ Requirements
- Python 3.8+
- Install dependencies:
  ```bash
  pip install PyMuPDF
````

---

## 📦 Installation

Clone this repository and install dependencies:

```bash
git clone https://github.com/Nahuelseoane/pdf-word-substituter.git
cd pdf-word-substituter
pip install -r requirements.txt
```

---

## 🚀 Usage

### **Run the script**

Edit the variables in `script.py`:

```python
file_name = "document"  # Name of the PDF (without extension)
text_to_replace = "Consumidor Final "
replacement_text = "Como estas Mecha "
```

Then run:

```bash
python script.py
```

The modified PDF will be saved as `updated_document.pdf` in your chosen path.

---

## 🖥 Code Overview

```python
import fitz  # PyMuPDF

file_name = "document"
pdf_path = f"/mnt/c/Users/jnahu/Downloads/{file_name}.pdf"
new_file_name = "updated_document"
output_path = f"/mnt/c/Users/jnahu/Downloads/{new_file_name}.pdf"
text_to_replace = "Consumidor Final "
replacement_text = "Como estas Mecha "

doc = fitz.open(pdf_path)

font_name = "helv"
font_size = 8
x_offset = 0
y_offset = 10

for page in doc:
    text_instances = page.search_for(text_to_replace)
    for inst in text_instances:
        rect = fitz.Rect(inst)
        text_info = page.get_text("dict")
        for block in text_info["blocks"]:
            for line in block.get("lines", []):
                for span in line.get("spans", []):
                    if text_to_replace in span["text"]:
                        font_name = span["font"]
                        font_size = span["size"]
                        break
        page.draw_rect(rect, color=(1, 1, 1), fill=(1, 1, 1))
        if font_name not in ["helv", "times", "cour"]:
            print(f"Warning: Font '{font_name}' not found. Using Helvetica instead.")
            font_name = "helv"
        x, y = inst[:2]
        page.insert_text((x + x_offset, y + y_offset), replacement_text,
                         fontsize=font_size, fontname=font_name, color=(0, 0, 0))

doc.save(output_path)
doc.close()
```

---

## 📂 Project Structure

```
pdf-word-substituter/
│
├── script.py            # Main script for PDF modification
├── requirements.txt      # Python dependencies
├── README.md             # Project documentation
└── output.pdf            # Example output file
```

---

## 🔧 Future Improvements

* Support for multiple replacements in one run.
* Improved font detection and embedding.
* GUI interface for easier use.

---

## 📜 License

This project is licensed under the [MIT License](LICENSE).

```
```
