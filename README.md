# Get babelNet synsets

It is a  python program for getting [babelNet](https://babelnet.org/) synsets in 3 languages: arabic, french and english. 

## Installing and requirements
You need to register to [babelNet](https://babelnet.org/register) and have a key to be able to use babelnet api.
you need to install [requests](http://docs.python-requests.org/en/master/user/install/).
```
pipenv install requests
```
You need to install AlphabetDetector
```
 pip install alphabet-detector
 ```
 
## How does it work
You need to have a list of french words like our test_dict file. One word per line.
Then we do the queries in babelnet to get the synsetsIds in babelnet.
With synsetids we can do 3 another queries to get the synsets in 3 languages : arabic, french and english.
We save these synsets in a different file.
One file per synset et per language.
