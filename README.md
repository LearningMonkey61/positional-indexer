
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

` 'term' : [ term_freq , { 'docID1' : [doc_freq, pos1, pos2, ...] , 'docID2' : [doc_freq, pos1, pos2] } ....]  `

The entire positonal index is a dictionary with terms as the keys whose corresponding value is a python list. The first index(0) of the list is the term frequency and the next index is a dictionary with keys as the docID's where the term occured and the value being a list whose first element, again, represents the document frequency and the corresponfing elements the position of the term in the document.


## workflow

### Running the program

* If you have pipenv, running `pipenv install` would simply install the require packages from pipfile.lock
* Otherwise just running `pip install nltk` would suffice.

The script works in the following way :

* From the docuemnt corpus, a single document is taken out and its body is preprocessed by using `nltk.TweetTokenizer` and removing '.' from the list of the tokens retruned. (For some reason, the tokenizer also counted '.' as a token)


