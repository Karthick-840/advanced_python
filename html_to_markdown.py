import os
from html2markdown import convert

def convert_html_to_markdown(input_file_path, output_folder_path, output_file_name="converted.md"):
  """
  Converts an HTML file to Markdown and saves it to a specified folder.

  Args:
      input_file_path (str): Path to the HTML file to be converted.
      output_folder_path (str): Path to the folder where the Markdown file will be saved.
      output_file_name (str, optional): Name of the output Markdown file. Defaults to "converted.md".

  Returns:
      None
  """

  try:
    # Construct input file path within "inputs" folder
    input_file_path = os.path.join("inputs", input_file_path)  # Assuming "inputs" folder is in the same directory

    # Read HTML content
    with open(input_file_path, "r") as f:
      html_content = f.read()

    # Convert HTML to Markdown
    markdown_content = convert(html_content)

    # Create output folder if it doesn't exist
    if not os.path.exists(output_folder_path):
      os.makedirs(output_folder_path)

    # Construct output file path
    output_file_path = os.path.join(output_folder_path, output_file_name)

    # Write Markdown content to output file
    with open(output_file_path, "w") as f:
      f.write(markdown_content)

    print(f"Successfully converted HTML to Markdown and saved to: {output_file_path}")

  except FileNotFoundError:
    print(f"Error: Input file '{input_file_path}' not found.")
  except Exception as e:
    print(f"An error occurred during conversion: {e}")

# Example usage
if __name__ == "__main__":
  input_file_path = "index.html"  # Assuming the HTML file is inside the "inputs" folder
  output_folder_path = "output"

  convert_html_to_markdown(input_file_path, output_folder_path)
