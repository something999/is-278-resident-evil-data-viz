from file_handler import *
import re # Identifies patterns (such as speaker indicators)

def replace_newline_characters(line: str) -> str:
    ''' Replaces all the newline characters with spaces. '''
    return line.replace('\n', ' ').replace('\r\n', ' ').replace('\r', ' ')

def replace_typewriter_space(line: str) -> str:
    ''' Replaces two spaces with a single space. '''
    return line.replace('  ', ' ')

def replace_quotation_marks(line: str) -> str:
    ''' Removes quotation marks. '''
    return line.replace('"', '')

def remove_stage_directions(line: str) -> str:
    ''' Removes stage directions (phrases contained within parentheses). '''
    return re.sub("\(.*\)", '', line)

def get_cleaned_line(line: str) -> str:
    ''' Standardizes line formats. '''
    line = replace_newline_characters(line)
    line = replace_typewriter_space(line)
    line = remove_stage_directions(line)
    line = replace_quotation_marks(line)
    return line
 
def get_dialogue(input: str) -> list:
    ''' Returns a list of lines representing direct game dialogue. '''
    dialogue = []
    with open(input, 'r', encoding = 'utf-8') as file:
        for line in re.finditer("^[A-Z]{1}[A-Za-z '.]+:{1}(.+[\n|\r\n|\r])*", file.read(), re.MULTILINE):
            line = get_cleaned_line(line.group(0))
            if (len(line[line.find(':') + 2:]) == 1): # Skip empty lines
                continue
            dialogue.append(line + '\n')
    return dialogue

def save_dialogue(output: str, dialogue: list) -> None:
    ''' Saves a list of lines to a file. '''
    with open(output, 'w', encoding = 'utf-8') as file:
        for line in dialogue:
            file.write(line)

def main():
    path = get_path_to_file('re5.txt', 'temp')
    dialogue = get_dialogue(path)
    save_dialogue(get_path_to_file('RE5_script.txt', 'temp'), dialogue)

main()