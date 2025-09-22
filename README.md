An algorythm to compress text efficiently
it is used to pretrain LLMs including GPT,BART,DeBARTa, and many more.

 
BPE iteratively replaces common pairs of bytes in text with a single new byte identifier, reducing sequence length while preserving information. These merges are stored in a dictionary lookup table (merges) that maps pairs to unique identifiers.

For decoding, the lookup table is used to reverse the merges by replacing identifiers with their original byte pairs to reconstruct the original text.
