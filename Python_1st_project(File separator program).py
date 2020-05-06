import os, shutil
#Dictionary
defined_extension = {
    'audio_extension': ('.mp3', '.wav', '.aif', '.cda'),
    'video_extension': ('.mp4', '.mov', '.wmv', '.flv', '.avi'),
    'document_extension': ('.docx', '.pdf', '.tex', '.txt', '.vtt', '.xlsx'),
    'image_extension': ('.jpeg', '.png')
}

User_folder_path = input("Enter Path:")

def files_finder(folder_path, folder_extension):
    files_list = []
    for file in os.listdir(folder_path):
        for extension in folder_extension:
            if file.endswith(extension):
                files_list.append(file)
    return files_list

for extension_type, extension_tuple in defined_extension.items():
    folder_name = extension_type.split('_')[0] + 'Files'
    folder_path = os.path.join(User_folder_path, folder_name)
    os.mkdir(folder_path)
    for item in files_finder(User_folder_path, extension_tuple):
        item_path = os.path.join(User_folder_path, item)
        item_new_path = os.path.join(folder_path, item)
        shutil.move(item_path, item_new_path)