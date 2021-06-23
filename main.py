#!/usr/bin/env python3

import os
import sys
from pathlib import Path


# health_center_acronym = sys.argv[1]
health_center_path = r"health center path"
test_path = r"test path"

replace_these_words = [

]

folders_to_exclude = [

]

for folder in os.listdir(health_center_path):
    # full_path = os.path.join(test_path, folder)
    full_path = os.path.join(health_center_path, folder)
    if os.path.isdir(full_path):

        if folder.lower() not in folders_to_exclude:
            Path(f"{full_path}/Archive").mkdir(parents=True, exist_ok=True)
            print(folder)

            for file in os.listdir(full_path):
                file_path = os.path.join(full_path, file)
                archive_file_path = os.path.join(full_path, "Archive", f"original-{file}")

                if file.startswith('cleaned'):
                    print('Already cleaned')
                    continue    #double check

                if file.endswith('.txt') or file.endswith('.csv'):
                    outfile = os.path.join(full_path, f"cleaned-{file}")

                    with open(os.path.join(full_path, file), encoding="utf8", errors='ignore') as fin, open(outfile, "w+") as fout:
                        for line in fin:
                            # line = line.lower() # makes everything lower case, easier to catch words but alters the file to lowercase.
                            for word in replace_these_words:
                             fout.write(line)
                    try:
                        os.rename(file_path, archive_file_path)
                    except:
                        print('error occurred ', sys.exc_info()[0])
                else:
                    pass

    else:
        pass
