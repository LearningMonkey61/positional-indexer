
# positional-indexer

[![Swapnil Sahu](https://img.shields.io/static/v1?label=status&message=work%20in%20progress&color=red&style=for-the-badge&logo=github "Swapnil Sahu")](https://github.com/LearningMonkey61)

A simple indexer designed for the Cranfield 1400 Dataset, which was precompiled, cleaned up and put into a JSON format.

``` json
    [
        ...
        {
          "id" : 163,
          "author" : "chapman,d.r.",
          "bibliography" : "nasa r-55, 1959.",
          "body" : "an analysis of the corridor and guidance requirements for supercircular entry planetary     atmospheres .   an analysis ... ",
          "title" : "an analysis of the corridor and guidance requirements..."
        },
        ...
    ]

```

The program uses the simple NLTK python module with it's implementation of Porter Stemmer and a tokenizer.

The index is realised in the following way :

`'term' : [ term_freq , { 'docID1' : [doc_freq, pos1, pos2, ...] , 'docID2' : [doc_freq, pos1, pos2] } ....]`

The entire positional index is a dictionary with terms as the keys whose corresponding value is a python list. The first index(0) of the list is the term frequency and the next index is a dictionary with keys as the docID's where the term occurred and the value being a list whose first element, again, represents the document frequency and the corresponding elements the position of the term in the document.


## workflow

### Running the program

* If you have pipenv, running `pipenv install` would simply install the require packages from pipfile.lock
* Otherwise just running `pip install nltk` would suffice.

The script works in the following way :

* From the document corpus, a single document is taken out and its body is preprocessed by using `nltk.TweetTokenizer` and removing '.' from the list of the tokens returned. (For some reason, the tokenizer also counted '.' as a token)
* All the tokens made are enumerated using the enumerate() method in python, giving us an integer value corresponding to the position of that token in that document. (Notice that StopWord removal, if done, should be done after this step, so that the correct positions are noted. We however have not removed the stopwords)
* Each token is then stemmed using a PorterStemmer provided by `nltk.PorterStemmer()`.
* The availability of the term is checked in a dictionary (our positional index), and if there, a further check is made to determine if the docID is in the list. If so the term frequency for that term(`positional-index[term][0]`) is increased by one and its position entered in the value list of the docID key, increasing the document frequency(`positional-index[term][1][docID][0]`) too. If the docID is not in the list, 1 and the first position is entered into the key as its value
* If the term is not in the positional-index, a new empty list is initialised and inserted as the value for the key (the term) and 1, {“docID” : [1,position] } is inserted into the list.
* Finally after repeating for all documents in the corpus, the positional-index is stored as a .txt file on the disk dumped using the  `json.dump()` method.
* The index can then be retrieved from disk and used to check the positions the given word occurs in 

## Shortcomings

* Preprocessing in this model is very very basic and would give ambiguous results for chained queries. The relevance queries given with the dataset if tested would give poor performance due to the lack of good pre-processing techniques. This can be overcome by using a more rigid token creation technique.  
* Index dumping into the .txt file with indentation provided by the json.dump() method bloats the file size a lot, Case in point, setting the indent parameter as 2 makes the index size as 7.1MB compared to the 2 MB when no indentation was used. Preferably no indentation should be used. But for purposes of readability, indentation was used here sacrificing small index size.
