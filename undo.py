#!/usr/bin/env python3

import os

# health_center_acronym = sys.argv[1]
health_center_path = r"health center path"
test_path = r"test path"

folders_to_exclude = [

]

for folder in os.listdir(test_path):
    full_path = os.path.join(test_path, folder)
    # full_path = os.path.join(health_center_path, folder)
    if os.path.isdir(full_path):

        if folder.lower() not in folders_to_exclude:

            for file in os.listdir(full_path):
                file_path = os.path.join(full_path, file)
                archive_file_path = os.path.join(full_path, "Archive", file)

                if file.startswith('cleaned'):
                    # print('Already cleaned')
                    # continue    #double check
                    os.rename(file_path, archive_file_path)
                    print('Moved cleaned filed to archive:')
                    # print(archive_file_path)

                if os.path.isdir(file_path):
                    for original_file in os.listdir(file_path):
                        if original_file.startswith('original'):
                            original_file_path = os.path.join(file_path, original_file)
                            back_to_main_folder = os.path.join(full_path, original_file)
                            # print('original_file_path ' + original_file_path)
                            # print(back_to_main_folder)
                            os.rename(original_file_path, back_to_main_folder) #renaming
                            print('Moved Original file out of archive')

                else:
                    pass

    else:
        pass
