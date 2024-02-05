from gtts import gTTS
from art import tprint
from pathlib import Path
import pdfplumber
import os


def pdf_to_mp3(file_path, language):
    try:
        if not os.path.isfile(file_path):
            raise FileNotFoundError(f'File {file_path} does not exist. Please check the Path')
        if not Path(file_path).suffix == '.pdf':
            raise ValueError(f'File {file_path} is not a PDF. Please provide a PDF file')

        print(f'[+] File {file_path}')
        print(f'[+] Language: {language}')
        print('[+] Processing(Be patient, it may take a few minutes, depending on the size of the pdf file)')

        with pdfplumber.open(file_path) as pdf:
            pages = [page.extract_text() for page in pdf.pages]
            text = ''.join(pages)
            text = text.replace('\n', '')

            audio = gTTS(text=text, lang=language, slow=False)
            file_name = Path(file_path).stem
            audio.save(f'{file_name}.mp3')

            return f'[+] {file_name}.mp3 saved successfully'
    except Exception as e:
        return str(e)


def main():
    tprint('PDF to MP3 converter', space=1)
    file_path = input(f'\n Enter a file path (for example: path/to/file.pdf. DO NOT USE " IN PATH): ')
    language = input(f'\n Enter a language (for example: "ru"): ')
    print(pdf_to_mp3(file_path, language))


if __name__ == '__main__':
    main()
