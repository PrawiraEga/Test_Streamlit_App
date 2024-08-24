import nltk

def download_nltk_pkg():
    packages = ['popular'
            ,'punkt'
            ,'averaged_perceptron_tagger'
            ,'wordnet'
            ,'sentiwordnet'
            ,'opinion_lexicon'
            ]

    #Download Packages
    for package in packages:
        nltk.download(package)

# print("All selected NLTK packages have been downloaded successfully.")