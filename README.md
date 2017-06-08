# TOPWords
python version of TOPWords model implementation

## Background
The unsupervised analysis of domain-specific texts is a popular area of NLP. The model of TOPWords initializes with an overcomplete 
dictionary and feeds the classic EM algorithm to analyze Chinese texts, and then rank and selecte the discovered words.

## Initialization
First run this line in the console.
```
pip install zhon
```
Then type in this line. And parameters can be changed/chosen in **Main.py**
```
python Main.py
```

## Description
*To be added.*

## Limitation Now
With the test text <chapter1.txt>, the model runs well. However, with the whole text <story_of_stone.txt> it runs quite slow. So 
either the ranking function, which is now 'significance score', need to be changed or some optimization need to be done.

## Future Work
Apply the model to a specific domain and make some improvements. 

*To be added.*
