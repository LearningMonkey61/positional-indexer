import json
import nltk 
import os
from nltk.tokenize import TweetTokenizer
from nltk.stem import PorterStemmer


def preprocessing(document_body): 
    tokenizer = TweetTokenizer() 
    token_list = tokenizer.tokenize(document_body) 
    token_list = [str for str in token_list if str !='.'] 

    return token_list 

def Indexer():
    stemmer = PorterStemmer()
    
    positional_index = {}
    
    with open('cranfield.json') as f :
        document_corpus = json.load(f) 

    for document in document_corpus :
        docID = document['id']
        tokens = preprocessing(document['body']) 
        for position, term in enumerate(tokens):
            term = stemmer.stem(term) 
            if term in positional_index : 
                positional_index[term][0] += 1
                if docID in positional_index[term][1] :
                    positional_index[term][1][docID][0] += 1
                    positional_index[term][1][docID].append(position)
                else:
                    positional_index[term][1][docID] = [1,position]
            else:
                positional_index[term] = []
                positional_index[term].append(1)
                positional_index[term].append({})
                positional_index[term][1][docID] = [1,position]
    
    if not os.path.exists('index.txt'):
        with open('index.txt', 'w') as fp:
            json.dump(positional_index, fp, indent=2)
    else:
        choice = input("Index Already created. Override? (Y|N)")
        if(choice == 'y' or choice == 'Y'):
            with open('index.txt', 'w') as fp:
                json.dump(positional_index, fp, indent=2)

    return positional_index

if __name__ == "__main__":
    print("Used Dataset for Indexing : Cranfield Dataset")
    print("Creating Index .....")
    stemmer = PorterStemmer()
    index = Indexer()
    print("Indexing done.  Index Size : " + str(os.path.getsize('index.txt') >> 20 ) + "MB")
    query = input("Enter Search Term : ")
    query = stemmer.stem(query)
    if query in index :
        print(index[query])
    else :
        print("Query term not found")

