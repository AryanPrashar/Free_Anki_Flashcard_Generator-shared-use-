# Anki Flashcard Generator from PDF Files

This zip file will generate Flashcards for **FREE** with no additional costs or limitations:

# Process Setup
Follow the steps below to setup this **Free PDF-to-Anki AI Pipeline:**

## Install Anki:
__Anki is the flashcard application where you'll study your generated cards.__

1. **Download Anki:** Go to the official Anki website: https://apps.ankiweb.net/
2. **Install Anki:** Download and install the correct version for your operating system (Windows, Mac, or Linux). Follow the installation prompts.

## Install the AnkiConnect Add-on

__This add-on allows other programs to connect with Anki, which is essential for our automated pipeline.__

1. **Open Anki:** Launch the Anki application.
2. **Go to Add-ons:** In the top menu bar, click on "Tools" and then select "Add-ons."
3. **Get Add-on Code:** A new window will appear. In the top-right corner, click "Get Add-ons..."
4. **Enter Code:** A small window will ask for a code. Enter the following code: 2055492159
5. **Install:** Click "OK" to install the add-on.
6. **Restart Anki:** Close and reopen Anki to complete the installation.

## Set Up the AI Flashcard Generator

__Now use my free, open-source GitHub project which uses AI to automatically create flashcards from your PDF files__

1. **Install Python:** If you don't have Python installed, download and install it from https://www.python.org/downloads/. During installation, make sure to check the box that says "Add Python to PATH."
2. **Click the green "Code" button** above and select "Download ZIP."
3. **Extract** the downloaded ZIP file to a location you'll remember, like your Desktop or Documents folder.
4. **Open your computer's command prompt** (on Windows, search for "cmd"; on Mac, search for "Terminal").
5. **Navigate to the project folder** you just extracted. For example, if it's on your desktop, you would type 
```shell
cd Desktop/Anki_FlashCard_Generator-main
```
and press Enter
6. **Install** the necessary Python libraries by typing 
```shell
pip install -r requirements.txt
```

## Generate Your Anki Flashcards

1. **Add Your PDFs:** Place the PDF lecture notes you want to convert into the "SOURCE_DOCUMENTS" folder within the project directory.
2. **Run the Script:** In the same command prompt/terminal window, run the script by typing python main.py and pressing Enter.
3. **Find Your Flashcards:** The script will process your PDFs and create a file named flashcards.txt

## Import Flashcards into Anki

1. **Open Anki:** If it's not already open, launch the Anki application.
2. **Create a New Deck:** Click the "Create Deck" button at the bottom of the main window and give your new deck a name (e.g., "Lecture Flashcards").
3. Go to "File" > "Import..."
4. **Select** the flashcards.txt file you generated.
5. An import window will appear. Make sure the "Deck" is set to the one you just created.
6. **Click** "Import."

You have now successfully created a pipeline to turn your PDFs into Anki flashcards!




















