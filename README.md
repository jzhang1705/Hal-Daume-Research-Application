# Hal-Daume-Research-Application

## How to Compile the Code:
To compile the code, go to the directory and type ```python3 TopTenCounter.py file.txt``` or ```python3 TopTenManuel.py file.txt``` where ```file.txt``` is any file in the directory. 

## Descriptions and Test Examples:
```TopTenCounter.py``` displays the top 10 common words through a dictionary without accounting for ties. It is coded using the counter class from the collections module. Most of the code is inspired from this site: https://www.geeksforgeeks.org/find-k-frequent-words-data-set-python/
``` 
(base) Jeffreys-MacBook-Pro:116654388 jeffreyzhang$ python3 TopTenCounter.py RandomWords1.txt
[('is', 2), ('a', 2), ('doing', 2), ('Life', 1), ('like', 1), ('dream', 1), ('Johns', 1), ('Hopkins', 1), ('University', 1), ('interesting', 1)]
(base) Jeffreys-MacBook-Pro:116654388 jeffreyzhang$ python3 TopTenCounter.py RandomWords.txt
[('Life', 1), ('is', 1), ('good', 1), ('People', 1), ('need', 1), ('to', 1), ('calm', 1), ('down', 1), ('Gratitude', 1), ('improves', 1)]
(base) Jeffreys-MacBook-Pro:116654388 jeffreyzhang$ python3 TopTenCounter.py DeclarationOfIndependence.txt 
[('of', 78), ('the', 76), ('to', 64), ('and', 55), ('our', 25), ('for', 20), ('their', 20), ('has', 20), ('in', 18), ('He', 18)]
```
