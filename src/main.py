from tokenizer import encode , decode 
from pathlib import Path

def main():
    


    file_path = Path(__file__).parent.parent / 'alice.txt'
    with file_path.open('r') as f:
        text = f.read()                                               #storing text file contents into text varaible



    encoded_ids,merges=encode(text)                                   #encode text into excoded_ids and save changes into merges
    print(len(encoded_ids))


    decoded_ids=decode(encoded_ids,merges)
    print(len(decoded_ids))


    if list(map(int,text.encode('utf-8'))) == decoded_ids: print('decoding completed successfully')   #check if message was decoded perfectly
    else: print('failed decoding')



#remove the triple quotes to write output.txt

 '''   output_path = Path(__file__).parent.parent / 'output.txt'                #getting path for output.txt
    with output_path.open('w') as f:                                         #creating and writing in output.txt
        f.write('\n------------------encoded--------------\n')
        f.write(','.join(map(str, encoded_ids)))                             #storing encoded data
        f.write('\n-----------decoded--------------\n')
        f.write(','.join(map(str,decoded_ids)))                              #storing decoded data      '''


main()
