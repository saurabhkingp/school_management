def open_file():
    global filepath, filelist 
    filepath=filedialog.askdirectory(title="Select a Directory")
    filelist =[]
    for root, dirs, files in os.walk(filepath):
        for file in files:
            if(file.endswith(".yaml")):
                filelist.append(os.path.join(root,file))
