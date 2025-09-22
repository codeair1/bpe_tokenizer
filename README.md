An algorithm to compress text efficiently.
 It is used to pretrain LLMs including GPT,BART,DeBARTa, and many more.

 
BPE iteratively replaces common pairs of bytes in text with a single new byte identifier, reducing sequence length while preserving information. These merges are stored in a dictionary lookup table (merges) that maps pairs to unique identifiers.

For decoding, the lookup table is used to reverse the merges by replacing identifiers with their original byte pairs to reconstruct the original text.



run 'src/main.py' to find length of encoded alice.txt data and length of decoded alice.txt data (takes some time to run as txt file is big)
remove comment from main.py to write output.txt again 
