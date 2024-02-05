PDF to MP3 Converter
This is my second project, do not judge strictly
This project is a simple tool for converting text from PDF files to MP3 audio files. It can be useful for creating audiobooks from PDF files or for listening to documents instead of reading.

Dependencies
The project uses the following Python libraries:

GTTs (Google Text-to-Speech) for converting text to audio.
pdfplumber for extracting text from PDF files.
pathlib for working with file paths.
art for beautiful text output to the console.
Make sure that all these libraries are installed on your system. You can install them using pip:

pip install -r requirements.txt

Using
To use this tool, just run the script pdf_to_mp3.py from the command line:

python pdf_to_mp3.py

The script will ask you for the path to the PDF file and the language for converting text to audio. After that, it converts the text from the PDF file to audio and saves it to an MP3 file with the same name as the original PDF file.

Error handling
The script includes exception handling for cases where the file does not exist or is not a PDF file. If any other error occurs, it will also be intercepted and returned to the user. This helps to better understand what went wrong if the script does not work as expected.

Support
If you have any problems or questions, do not hesitate to contact us. I'm always happy to help!
