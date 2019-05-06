# importing os module 
import os 
  
path = ''

files = []
# r=root, d=directories, f = files
for r, d, f in os.walk(path):
    for file in f:
        if '.txt' in file:
            files.append(os.path.join(r, file))

for f in files:
    print(f)

os.rename('a.txt', 'b.kml')

#links de apoio 
#https://www.mkyong.com/python/python-how-to-list-all-files-in-a-directory/
#https://stackoverflow.com/questions/2491222/how-to-rename-a-file-using-python