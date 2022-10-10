'''this will format my payslip'''
import os
from formatter import format_15, format_30



def get_text_lines(file):
    with open(file, 'rt') as file:
        return file.readlines()

def get_files(dir):
    files = os.listdir()
    files = [file for file in files if '15' in file]
    return files


def main():
    files = get_files(os.curdir)

    for file in files:
        lines = [line for line in get_text_lines(file) if line != '\n']
        file_name, file_ext = os.path.splitext(file)

        print('Processing {}'.format(file))


        with open(file_name + 'formatted' + file_ext, 'wt') as file_handle:
            for idx,line in enumerate(lines):
                try:
                    file_handle.write(format_15[idx](*line.strip().split()))
                except TypeError as e:
                    print(e)
                    continue
        print('Finished {}'.format(file))




if __name__ == '__main__':
    main()


