import os
import shutil
from docx import Document
from docx.shared import Pt
from datetime import datetime
# from pptx import Presentation

# def replace_placeholders_in_pptx(pptx_path, folder_name, replacement_text):
#     presentation = Presentation(pptx_path)

#     # Assuming you want to replace text in the second slide
#     slide_index = 2  # Indexing starts from 0

#     slide = presentation.slides[slide_index]

#     # Iterate through all shapes in the slide
#     for shape in slide.shapes:
#         if hasattr(shape, "text"):
#             # Replace '||||||||||||||||' with folder_name
#             shape.text = shape.text.replace('||||||||||||||||', folder_name)

#             # Replace '|||||||||||||||||||||||||||||' with replacement_text
#             shape.text = shape.text.replace('|||||||||||||||||||||||||||||', replacement_text)

#     return presentation

def create_folder_and_copy_ppt_and_word(source_folder, folder_name, ppt_file_path, word_file_path):

    # SUKURIA NAUJĄ FOLDERĮ, ŠIUO ATVEJU "KLIENTS" FOLDERYJE
    folder_path = os.path.join(source_folder, folder_name)
    os.makedirs(folder_path, exist_ok=True)

    # NUSIKOPIJUOJA POWERPOINT PREZENTACIJOS VARDĄ
    ppt_filename = os.path.basename(ppt_file_path)
    ppt_name, ppt_extension = os.path.splitext(ppt_filename)

    # word_filename = os.path.basename(word_file_path)
    # word_name, word_extension = os.path.splitext(word_filename)

    # SUKURIA NAUJĄ NUKOPIJUOTO IR ĮKLIJUOTO PPT FAILO VARDĄ
    new_ppt_filename = f"{folder_name}_{ppt_name}{ppt_extension}"
    # new_word_filename =  f"{folder_name}_{word_name}{word_extension}"

    # SUKONSTRUOJA KELIĄ NUOKIPIJUOTAM FAILUI KAD JIS BŪTŲ ĮKLIJUOTAS I NAUJAI SUKURTĄ FOLDERĮ
    destination_ppt_path = os.path.join(folder_path, new_ppt_filename)
    # destination_word_path = os.path.join(folder_path, new_word_filename)


    # NUKOPIJUOJA TEMPLATE FAILĄ IR JAM UŽDEDĄ PASIRINKTĄ VARDĄ 
    shutil.copy2(ppt_file_path, destination_ppt_path)
    # # shutil.copy2(word_file_path, destination_word_path)
    # replaced_presentation = replace_placeholders_in_pptx(destination_ppt_path, folder_name, 'Vardeni Pavardeni')

    # # Save the modified presentation
    # modified_pptx_path = destination_ppt_path.replace('.pptx', '_modified.pptx')
    # replaced_presentation.save(modified_pptx_path)

    word_template = Document(word_file_path)

    # Replace placeholders in Word document
    for paragraph in word_template.paragraphs:
        if 'COMPANY_NAME'.strip() in paragraph.text.upper():
            for run in paragraph.runs:
                if 'COMPANY_NAME'.strip() in run.text.upper():
                    run.text = run.text.replace('COMPANY_NAME', folder_name)

        if '@date' in paragraph.text:
            for run in paragraph.runs:
                if '@date' in run.text:
                    run.text = run.text.replace('@date', datetime.today().strftime('%Y-%m-%d'))



    new_word_filename = f"{folder_name.strip().replace(' ', '_')}_PROGRESS_TRACKING.docx"
    destination_word_path = os.path.join(folder_path, new_word_filename)
    word_template.save(destination_word_path)

    print(repr(new_word_filename))


if __name__ == '__main__':
    specified_folder = 'C:\\Users\\PetrasAnksaitis\\OneDrive - transol.lt\\Docs_Vaidotas_Petras\\KLIENTAI\\KONTAKTUOTI'
    # specified_folder = "C:\\Users\\PetrasAnksaitis\\Downloads"
    specified_folder_name = 'INCHCAPE LIETUVA'
    powerpoint_file_path = "C:\\Users\\PetrasAnksaitis\\OneDrive - transol.lt\\Docs_Vaidotas_Petras\\KLIENTAI\\_EPITCH UNISHOP.pptx"
    word_file_path = "C:\\Users\\PetrasAnksaitis\\OneDrive - transol.lt\\Docs_Vaidotas_Petras\\KLIENTAI\\PROGRESS TRACKING.docx"

    create_folder_and_copy_ppt_and_word(specified_folder, specified_folder_name, powerpoint_file_path, word_file_path)