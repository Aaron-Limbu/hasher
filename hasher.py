import hashlib
import sys
import argparse

MAX = int(636)
strings = []
nstrings = []

def prompt_user_input():
    while True:
        uinput = input('Enter file name: ').strip()
        name = uinput.split('.')
        if len(name) > 1 and name[1].lower() == 'txt':
            break
        else:
            print('Enter proper file name with .txt extension.')
    return uinput 

def hashfile(file, method):
    B_size = 66666
    if method == 1: 
        hasher = hashlib.sha512()
    elif method == 2: 
        hasher = hashlib.md5()
    elif method ==3 : 
        hasher = hashlib.sha224()
    elif method == 4: 
        hasher = hashlib.sha3_224()
    elif method == 5: 
        hasher = hashlib.sha3_512()
    else:
        raise ValueError("Invalid method. Use 1 for SHA-512 and 2 for MD5.")

    with open(file, "r", encoding="ISO-8859-1") as rfile:
        for line in rfile:
            strings.append(line)
            hasher.update(line.encode('ISO-8859-1'))
            nstrings.append(hasher.hexdigest())
                
def write_output(output_file):
    if output_file:
        with open(output_file, 'w') as ofile:
            for hash_string in nstrings:
                ofile.write(f'{hash_string}\n')
    else:
        for hash_string in nstrings:
            print(hash_string)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Hashes your text file\n")
    parser.add_argument('-i', '--input', type=str, help='Input the file, example: a.txt\n')
    parser.add_argument('-o', '--output', type=str, help='Output file name\n')
    parser.add_argument('-m', '--method', type=int, help='Hash method: 1 for SHA-512, 2 for MD5\n', required=True)
    args = parser.parse_args()
    
    if args.input:
        in_file = args.input
    else:
        in_file = prompt_user_input()
        
    hashfile(in_file, args.method)
    
    write_output(args.output)
