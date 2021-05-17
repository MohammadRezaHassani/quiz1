
class FileDateLog:
    def __init__(self, filepath, mode):
        self.file_path = filepath
        self.open_time = datetime.datetime.now()
        self.file = None
        self.close_time = None
        self.mode = mode

    def __enter__(self):
        self.file = open(self.file_path, self.mode)
        self.re_write()
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()
        if exc_val:
            self.re_write()
            self.append_time()
            print("Some Exception Happend")
            return True
        self.append_time()

    def re_write(self):
        my_file = open(self.file_path)
        content = my_file.readlines()
        my_file.close()
        my_file = open(self.file_path, "w")
        for line in range(len(content) - 2):
            my_file.write(content[line])

        my_file.close()

    def append_time(self):
        self.close_time = datetime.datetime.now()
        self.file = open(self.file_path, "a")
        self.file.write(f"\nlast open time in {self.open_time}\n")
        self.file.write(f"last close time  in {self.close_time}\n")
        self.file.close()


with FileDateLog("hello.txt", "a") as hello:
    hello.write("eyvay del man\n")





