
# positional-indexer

[![Swapnil Sahu](https://img.shields.io/static/v1?label=status&message=work%20in%20progress&color=red&style=for-the-badge&logo=github "Swapnil Sahu")](https://github.com/LearningMonkey61)

####  WEB SEARCH AND MINING ASSIGNMENT
__Team Members__

>Swapnil Sahu [B118061]

>Swapnil Kole [B118060]

>Shubham Mishra [B118058]

>Shubham Hazra [B118057]

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

The program uses the simple NLTK python module with it's  implementation of Porter Stemmer and a tokenizer.

The index is realised in the following way : 

` 'term' : [ term_freq , { 'docID1' : [doc_freq], pos1, pos2, ... } ....]  `

The entire positonal index is a dictionary with terms as the keys whose corresponding value is a python list. The first index(0) of the list is the term frequency and the next index is a dictionary with keys as the docID's where the term occured and the value being a list whose first element, again, represents the document frequency and the corresponfing elements the position of the term in the document.
