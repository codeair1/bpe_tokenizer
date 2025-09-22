from tokenizer import encode , decode 

def main():
    text = 'testing longer paragraph now  In this video I explain Byte-Pair Encoding, which is the sub-word tokenization algorithm used by GPT. In other words, its an algorithm for converting text into numbers. Lets dive in.But wait, theres more! In the next video, were going to be coding up BPE in Python, from scratch. So stay tuned '

    encoded_ids,merges=encode(text)     #encode text into excoded_ids and save changes into merges
    print(len(encoded_ids))
    decoded_ids=decode(encoded_ids,merges)
    print(len(decoded_ids))
    if list(map(int,text.encode('utf-8'))) == decoded_ids: print('decoding completed successfully')   #check if message was decoded perfectly
    else: print('failed decoding')



main()