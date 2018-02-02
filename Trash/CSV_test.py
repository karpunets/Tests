import codecs

def convert_to_utf_8(fileName):
    f = codecs.open(fileName, 'r', 'cp1251')
    u = f.read()  # now the contents have been transformed to a Unicode string
    new_file_path = fileName + "_converted.csv"
    out = codecs.open(new_file_path, 'w', 'utf-8')
    out.write(u)  # and now the contents have been output as UTF-8
    out.close()
    return new_file_path

def checkFile(filePath):
    filePath = filePath + ".csv"
    file = convert_to_utf_8(filePath)
    f= open(file, encoding="utf-8")
    for i in f:
        print(i)

checkFile("xls_from_Radion")