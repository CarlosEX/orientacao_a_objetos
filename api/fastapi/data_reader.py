import pandas as pd

class DataCsv:

    def get_all(self, lines: int) -> str:
        # path = './api/fastapi/data/data.csv'
        path = 'https://gist.githubusercontent.com/curran/a08a1080b88344b0c8a7/raw/0e7a9b0a5d22642a06d3d5b9bcbad9890c8ee534/iris.csv'
        # path = 'https://github.com/thephpleague/csv/blob/master/test_files/prenoms.csv' 
        df = pd.read_csv(path, header= None)
        
        return df.head(lines)

