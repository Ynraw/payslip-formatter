'''copy pasting from a pdf file will remove all the formatting so i made a 
    command line app that will format my payslip to be readable.'''
    
import os
from formatter import format_header, format_content, format_summary
from argparse import ArgumentParser


def get_text_lines(file):
    with open(file, 'rt') as file:
        return file.readlines()

def get_files(dir):
    files = os.listdir()
    files = [file for file in files if '_ps' in file]
    return files


def main(file):
    
    lines = [line for line in get_text_lines(file) if line != '\n']
    file_name, file_ext = os.path.splitext(file)

    print('Processing {}'.format(file))


    with open(file_name + '_format' + file_ext, 'wt') as file_handle:
        for idx,line in enumerate(lines):
            if format_header.get(idx):
                file_handle.write(format_header.get(idx)(*line.strip().split()) + '\n')
            elif format_content.get(idx):
                file_handle.write(format_content.get(idx)(*line.strip().split()) + '\n')
            else:
                file_handle.write(format_summary.get(idx)(*line.strip().split()) + '\n')
                
    print('Finished {}'.format(file))



if __name__ == '__main__':
 
    my_parser = ArgumentParser(prog='',
                           usage='Command line application to format my payslip as textfile')
    my_parser.add_argument('-f', '--file', type=str, default=None, help='specify file to be formatted')
    args = my_parser.parse_args()

    main(args.file)