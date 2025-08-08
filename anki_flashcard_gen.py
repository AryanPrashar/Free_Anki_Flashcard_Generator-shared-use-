import os
import fitz #PyMuPDF library
import requests

# This function reads the PDF (edit is not generally required)

def read_pdf(file_path):

    try:
        with fitz.open(file_path) as pdf:
            text = ""
            for page in pdf:
                text += page.get_text()
        return text)
    except Exception as e:
        print(f"Error reading PDF file: {e}")
        return None

    # This is the main function that generates the flashcards

def create_anki_cards(pdf_text, output_file):
    print("Creating Anki cards...")

    # EDITABLE: The AI's Prompt for generating flashcards:

    prompt = f"""

    You are an expert Anki flashcard creator. Your task is to read the provided text and create EXACTLY 20 flashcards.

        OUTPUT RULES — You must follow these exactly:
        1. The output must be EXACTLY 20 lines.
        2. Each line must be in the format:
            front ; back
            - One space before and after the semicolon.
        3. DO NOT number, bullet, label, or prefix the lines in any way.
        4. DO NOT add any extra text before or after the 20 lines.
        5. Each "front" must be ONE of these styles:
             - **Fill-in-the-Blank:** A sentence with a missing key term represented by four underscores `____`. (Ex. The capital city of Japan is ____ ; Tokyo)
             - **Direct Question:** A short, clear question about a key concept, fact, or process. (What is the chemical symbol for gold? ; Au)
             - **Term/Definition:** A single important term. (Mitochondria ; Organelles that produce energy for the cell through respiration)
        6. Each "back" must:
             - For Fill-in-the-Blank: ONLY the missing term.
             - For Question: ONLY the precise, concise answer.
             - For Term/Definition: ONLY the definition of that term.
        7. Each flashcard must be unique, non-redundant, and based ONLY on the provided text. Try to cover a variety of important concepts from the text with a variety of difficulties.
        8. DO NOT include hints, explanations, examples, or commentary — ONLY the flashcards in the exact format.

        Now, create exactly 20 flashcards based ONLY on this text:

    {pdf_text}
    """

    try:

         # EDITABLE VARIABLE: AI Model Name (Ollama, Model Name: mistral, is currently in use. You must have this model)
         # Change model name if you have a different one installed.

        response = requests.post(
            'http://localhost:11434/api/generate',
            json={
                'model': 'mistral',
                'prompt': prompt,
                'stream': False
            },

             # EDITABLE VARIABLE: Request Timeout (maximum number of seconds the script will wait for the AI to respond)

            timeout=900
        )
        response.raise_for_status()

        full_response = response.json().get('response', '')

        if full_response:
            lines = [line.strip() for line in full_response.split("\n") if line.strip()]

            # EDITABLE VARIABLE: Number of Flashcards (To get # flashcards instead of 20, change 'lines[:20]' to 'lines[:#])

            lines = lines[:20] 
            outfile.write("\n".join(lines) + "\n\n")
            print(f"  > Successfully processed and added 20 flashcards.")
        else:
            print("  > Warning: AI model returned an empty response.")

    except requests.exceptions.ConnectionError:
        print("\n--- ERROR ---")
        print("Could not connect to Ollama. Please make sure the Ollama application is running.")
        exit()
    except requests.exceptions.ReadTimeout:
        print("  > Error: The request timed out. The AI model took too long to respond.")
    except Exception as e:
        print(f"  > An unexpected error occurred: {e}")

        # Runs main function (accessing 'SOURCE_DOCUMENTS' folder, reading PDFs, and creating Anki cards)

if __name__ == "__main__":
    ROOT_DIRECTORY = os.path.dirname(os.path.realpath(__file__))

    # EDITABLE VARIABLE: Source Folder Name (If you wanted to rename your folder, you would change "SOURCE_DOCUMENTS" to "YourName" here)

    source_folder = os.path.join(ROOT_DIRECTORY, "SOURCE_DOCUMENTS")

    try:
        pdf_files = [f for f in os.listdir(source_folder) if f.lower().endswith('.pdf')]
    except FileNotFoundError:
        print("ERROR: The 'SOURCE_DOCUMENTS' folder was not found.")
        exit()

    if not pdf_files:
        print("No PDF files found in the 'SOURCE_DOCUMENTS' folder.")
    else:
        print(f"Found {len(pdf_files)} PDF(s) to process: {', '.join(pdf_files)}")
        
        # EDITABLE VARIABLE: Output File Name (If you wanted to rename your flashcard text file, you would change "flashcards.txt" to "YourName" here)

        output_filename = "flashcards.txt"
        
        with open(output_filename, "w", encoding='utf-8') as outfile:
            for pdf_file in pdf_files:
                full_path = os.path.join(source_folder, pdf_file)
                print(f"\n--- Processing: {pdf_file} ---")
                
                pdf_text = read_pdf(full_path)
                
                if pdf_text:
                    create_anki_cards(pdf_text, outfile)
                else:
                    print(f"  > Skipping {pdf_file} due to a reading error.")
                    
        print(f"\n--- ALL DONE! ---")
        print(f"All flashcards have been saved to '{output_filename}'. You can now import this file into Anki.")

