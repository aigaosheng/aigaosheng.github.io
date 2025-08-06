import os

folder_path = './_posts'  # 🔁 change this to your folder path
ofolder_path = './posts' 
html_files = []

rm_list = ["author:",
  "login: c013a2015",
  "email: c013a2015@gmail.com",
  'display_name: sheng gao',
  'first_name: sheng',
  'last_name: gao'
]
# Walk through the folder and find all .html files
for root, dirs, files in os.walk(folder_path):
    for file in files:
        if file.endswith('.html'):
            file_path = os.path.join(root, file)
            print(file)
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read().split("\n")
                content = list(filter(lambda x: x not in rm_list, content))

                with open(os.path.join(ofolder_path, file), 'w') as fo:
                    fo.write("\n".join(content))


                # break

