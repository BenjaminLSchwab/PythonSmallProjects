import sqlite3

connection = sqlite3.connect("test.db")

with connection:
    cursor = connection.cursor()

    cursor.execute(""" CREATE TABLE IF NOT EXISTS tbl_files (
                                        id integer PRIMARY KEY,
                                        col_file text NOT NULL
                                    ); """)
    connection.commit()

    fileList = ('information.docx','Hello.txt','myImage.png', \
            'myMovie.mpg','World.txt','data.pdf','myPhoto.jpg')

    for file in fileList:
        if file.find(".txt") != -1:
            cursor.execute("INSERT INTO tbl_files(col_file) VALUES(?)", (file,))
            print("{}\n".format(file))

    connection.commit()

    cursor.execute("SELECT * FROM tbl_files")
    varFiles = cursor.fetchall()
    for item in varFiles:
        print(item)
connection.close()