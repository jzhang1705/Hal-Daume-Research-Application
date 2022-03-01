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

```TopTenManual.py``` displays the top 10 common words manually while accounting for ties within the rank of 10. It displays the rank (tied rank), word, and the frequency of the word in the terminal

```
(base) Jeffreys-MacBook-Pro:116654388 jeffreyzhang$ python3 TopTenManual.py DeclarationOfIndependence.txt 
1: of 78
2: the 76
3: to 64
4: and 55
5: our 25
6: for 20
6: their 20
6: has 20
9: in 18
9: He 18
(base) Jeffreys-MacBook-Pro:116654388 jeffreyzhang$ python3 TopTenManual.py RandomWords.txt 
1: Life 1
1: is 1
1: good 1
1: to 1
1: need 1
1: People 1
1: sad 1
1: us 1
1: makes 1
1: Ingratitude 1
1: calm 1
1: down 1
1: Gratitude 1
1: improves 1
1: overall 1
1: happiness 1
(base) Jeffreys-MacBook-Pro:116654388 jeffreyzhang$ python3 TopTenManual.py RandomWords1.txt 
1: is 2
1: a 2
1: doing 2
4: Life 1
4: Johns 1
4: dream 1
4: disorders 1
4: health 1
4: mental 1
4: of 1
4: Hopkins 1
4: University 1
4: like 1
4: interesting 1
4: research 1
4: On 1
4: stuff 1
4: illegalized 1
4: by 1
4: Richard 1
4: Nixon 1
4: The 1
4: work 1
4: they're 1
4: shows 1
4: promise 1
4: in 1
4: curing 1
4: wide 1
4: range 1
```
