import json


def extract_markdown_from_ipynb(file_path):
    """
    Extrae los textos en formato Markdown de un archivo Jupyter Notebook (.ipynb).

    Args:
        file_path (str): Ruta del archivo .ipynb.

    Returns:
        list: Lista de strings con los textos en Markdown.
    """
    with open(file_path, "r", encoding="utf-8") as f:
        notebook_data = json.load(f)

    markdown_cells = []

    # Recorrer las celdas del notebook
    for cell in notebook_data.get("cells", []):
        if cell.get("cell_type") == "markdown":
            markdown_cells.append("".join(cell.get("source", [])))

    return markdown_cells


def save_markdown_to_txt(markdown_texts, output_file):
    """
    Guarda los textos Markdown extraídos en un archivo .txt.

    Args:
        markdown_texts (list): Lista de textos en Markdown.
        output_file (str): Ruta del archivo .txt de salida.
    """
    with open(output_file, "w", encoding="utf-8") as f:
        for i, text in enumerate(markdown_texts, start=1):
            f.write(f"Markdown Cell {i}:\n{text}\n{'-'*40}\n")


# Ruta al archivo .ipynb
file_path = "./EV1/EV_1_Gonzalo_Cayunao_Erices.ipynb"

# Extraer textos Markdown
markdown_texts = extract_markdown_from_ipynb(file_path)

# Ruta al archivo de salida .txt
output_file = "markdown_output.txt"

# Guardar los textos en un archivo .txt
save_markdown_to_txt(markdown_texts, output_file)

print(f"Los textos Markdown se han guardado en {output_file}.")
