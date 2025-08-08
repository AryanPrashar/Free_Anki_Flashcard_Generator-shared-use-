# Anki Flashcard Generator from PDF Files

This zip file will generate Flashcards for **FREE** with no additional costs or limitations:

The process has two main parts:
Part 1: The One-Time Setup: Installing all the necessary free software.
Part 2: Your Reusable Workflow: The simple steps you'll follow each time you want to create new flashcards.

# Part 1: The One-Time Setup
You only need to do these steps **ONCE**

## Install Anki:
__Anki is the flashcard application where you'll study your generated cards.__

1. **Download Anki:** Go to the official Anki website: https://apps.ankiweb.net/
2. **Install Anki:** Download and install the correct version for your operating system (Windows, Mac, or Linux). Follow the installation prompts.

## Set Up the AI Flashcard Generator

__Now use my free, open-source GitHub project which uses AI to automatically create flashcards from your PDF files__

1. **Install Python:** If you don't have Python installed, download and install it from https://www.python.org/downloads/. During installation, make sure to check the box that says "Add Python to PATH."
2. **Click the green "Code" button** above and select "Download ZIP."
3. **Extract** the downloaded ZIP file to a location you'll remember, like your Desktop or Documents folder.
4. **Place** this unzipped folder somewhere convenient, like your Desktop.

## Install and Set Up the Local AI (Ollama)

__This is the "brain" that will create your flashcards. It runs 100% on your own computer, so it's free and private.__

1. **Go** to the Ollama website: https://ollama.com/
2. **Download** and install Ollama for your operating system.
3. **After it's installed,** Ollama will run in the background. Now, you need to download a specific AI model for it to use.
4. **Open** your computer's command line tool:
            **Windows:** Press the Windows Key, type cmd, and press Enter.
            **Mac:** Press Command + Spacebar, type Terminal, and press Enter.
5. **In the black window** that appears, type the following command and press Enter. This downloads the "Mistral" AI model (it's a few gigabytes and may take a few minutes).

```shell
ollama run mistral
```

## Install the Required Python Libraries

1. Open a new command line window (cmd or Terminal).
2. Install the PDF reader library by running this command:
```shell
pip install PyMuPDF
```
3. Install the requests library by running this command:
```shell
pip install requests
```
###Setup is complete! You are now ready to start creating flashcards.

#Part 2: Your Reusable Flashcard Workflow

## Make Sure the AI is Running

__The Ollama application must be running in the background. Check for its icon in your system tray (bottom-right on Windows) or menu bar (top-right on Mac). If it's not running, just launch the Ollama application.__

## Make Sure the AI is Running

1. Open the project folder you downloaded:
```shell
Free_Anki_FlashCard_Generator-shared-use--main.
```
4. **Inside**, find the folder named **SOURCE_DOCUMENTS**
5. **Place** any and all PDF files you want to convert into this folder.

## Run the Script

1. **Open** your command line tool (cmd or Terminal).
2. **You need to tell the command line** to navigate to your project folder. Type cd (the letters c and d followed by a space).
3. **Now**, find your project folder (Free_Anki_FlashCard_Generator-shared-use--main) on your computer, and drag and drop the folder icon directly into the command line window. This will automatically paste its full path.
4. **Press Enter.** Your command prompt should now show you are inside the project folder.
5. **Run the script** by typing the following command and pressing **Enter:**
```shell
python Anki_flashcards_creator.py
```
6. **Be patient.** The script will now start processing. Depending on your computer's speed and the length of your PDFs, this can take several minutes. You can watch the progress in the command line window.
7. **When it's finished,** it will say --- ALL DONE! ---. Inside your project folder, you will now find a new file named flashcards.txt.

## Import into Anki

1. **Open** the Anki application.
2. **Click** "Create Deck" at the bottom and give it a name (e.g., "Biology Lecture 1").
3. **Click** on your new deck to select it.
4. **Go** to File > Import...
5. **Select** the flashcards.txt file from your project folder.
6. **An import window will appear.** This step is critical:
            **Make sure** "Fields separated by:" is set to Semicolon.
            **Make sure** the option "Allow HTML in fields" is checked.
7. **Click** the "Import" button.

Congratulations! Your automatically generated flashcards are now in Anki
