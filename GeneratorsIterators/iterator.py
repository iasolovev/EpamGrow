import os


class FileIterator:
    def __init__(self, directory):
        self.directory = directory
        self.file_names = os.listdir(directory)

    def __iter__(self):
        self.len = len(self.file_names)
        self.next_index = -1
        return self

    def __next__(self):
        if self.next_index < self.len - 1:
            self.next_index += 1
            return self.file_names[self.next_index]
        else:
            raise StopIteration


if __name__ == '__main__':
    file_iterator = FileIterator('C:/')
    for file_name in file_iterator:
        print(file_name)
