import fitz  # PyMuPDF

pdf_path = "/mnt/c/Users/jnahu/Downloads/updated_document4.pdf"
output_path = "/mnt/c/Users/jnahu/Downloads/updated_document5.pdf"
text_to_replace = "Consumidor Final "
replacement_text = "Como estas Mecha "

doc = fitz.open(pdf_path)

# Default values
font_name = 'helv'
font_size = 8
x_offset = 0  # Adjust horizontal positioning
y_offset = 10  # Move text down by 2 points (adjust as needed)

for page in doc:
    text_instances = page.search_for(text_to_replace)

    for inst in text_instances:
        rect = fitz.Rect(inst)

        # Extract text attributes (font size and font)
        text_info = page.get_text("dict")
        for block in text_info["blocks"]:
            for line in block.get("lines", []):
                for span in line.get("spans", []):
                    if text_to_replace in span["text"]:
                        font_name = span["font"]
                        font_size = span["size"]
                        break  # Stop at first match

        # Erase old text with a white rectangle
        page.draw_rect(rect, color=(1, 1, 1), fill=(1, 1, 1))

        # If PyMuPDF fails to find the font, default to Helvetica
        if font_name not in ["helv", "times", "cour"]:
            print(
                f"Warning: Font '{font_name}' not found. Using Helvetica instead.")
            font_name = "helv"  # Default to Helvetica
        # Insert new text at adjusted position
        x, y = inst[:2]  # Original position
        page.insert_text(
            (x + x_offset, y + y_offset), replacement_text,
            fontsize=font_size,
            fontname=font_name,
            color=(0, 0, 0)  # Black text
        )

# Save the modified file
doc.save(output_path)
doc.close()

print(
    f"Text replacement completed with font matching. Updated PDF saved as {output_path}")
