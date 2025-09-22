def get_stats(ids):
    counts = {}
    for pair in zip(ids , ids[1:]):                                     #iterates through all different pairs
        counts[pair] = counts.get(pair,0)+1                             # counts number of times pair appeared
    return counts


def merge(ids,pair,idx):
    newids = []
    i=0
    while i<len(ids):
        if i<len(ids)-1 and ids[i] ==pair[0] and ids[i+1] == pair[1]:    #checks if pair matches through the sequence
            newids.append(idx)                                        #puts idx instead of the pair and increments the byte by 2 to skip the pair indexes
            i=i+2
        else:
            newids.append(ids[i])                                 #pair did not match, hence placing the orignal byte and incrementing 1
            i=i+1
    ids= newids
    return ids

def encode(text):

    merges = {}
    ids = text.encode('utf-8')
    ids = list(map(int,ids))                                          #converting bytes to int values
    idx= 256                                                            #all int values from 0 to 255 are not available
    
                                                    
    while True:

        stats = get_stats(ids)                                       #finding pairs and how many times they appear
        if not stats:
            break;
        pair = max(stats, key=stats.get)                                #finding current max occurance of pair
        if stats[pair]  <=1:
            break                                                       #leave the loop only when all pairs are unique in the ids
        #print(f'merging {pair} into {idx}')        
        ids = merge(ids,pair,idx)                                           #merging the pairs of byte into a single byte
        merges[pair] = idx                                            #noting the byte value stored at pair's position
        idx =idx+1



    return ids,merges                                                    #return the new token and changes made in it stored in merges


def decode(ids,merges):

    for pair in reversed(merges):                                         #iterating through all merges completed during encoding in reverse order
        new_ids = []
        last_token = merges[pair]                                        #getting the last token
        i=0



        while i<len(ids):                                                #checking all bytes to find the token to convert to the pair
            if ids[i] == last_token:
                new_ids.extend(pair)                                      #replacing the token with pair
                i=i+1
            else:
                new_ids.append(ids[i])                                    #putting back the byte in place
                i=i+1
        ids = new_ids



    return ids