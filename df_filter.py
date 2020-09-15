def Snippet_106():
   
    print(format('How to search a value within a Pandas DataFrame column','*^82'))

    import warnings
    warnings.filterwarnings("ignore")

    # load libraries
    import pandas as pd
    raw_data = {'first_name': ['Jason', 'Jason', 'Tina', 'Jake', 'Amy'],
                'last_name': ['Miller', 'Miller', 'Ali', 'Milner', 'Cooze'],
                'age': [42, 42, 36, 24, 73],
                'preTestScore': [4, 4, 31, 2, 3],
                'postTestScore': [25, 25, 57, 62, 70]}

    df = pd.DataFrame(raw_data, columns = ['first_name', 'last_name', 'age',
                                           'preTestScore', 'postTestScore'])
    print(df)

    # Find where a value exists in a column
    # View preTestscore where postTestscore is greater than 50
    print(df['preTestScore'].where(df['postTestScore'] > 50))

Snippet_106()