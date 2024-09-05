import nltk

def download_nltk_pkg():
    packages = ['punkt'
            ,'punkt_tab'    
            ,'averaged_perceptron_tagger'
            ,'averaged_perceptron_tagger_eng'
            ,'wordnet'
            ,'sentiwordnet'
            ,'opinion_lexicon'
            ]

    #Download Packages
    for package in packages:
        nltk.download(package)

# print("All selected NLTK packages have been downloaded successfully.")
