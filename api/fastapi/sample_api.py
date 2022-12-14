from fastapi import FastAPI
from fastapi.responses import StreamingResponse
from data_reader import DataCsv
import pandas as pd


app = FastAPI()

@app.get('/')
def hello():
    return {'Hello World!'}

@app.get("/get-data")
def get_data():

    data = DataCsv()
    result = data.get_all(5)
    return result


@app.get("/my-first-api")
def hello_name(name = None):

    if name is None:
        text = 'Hello!'
    else:
        text = 'Hello ' + name + '!'

    return text

@app.get("/get-iris")
def get_iris():

    import pandas as pd
    url ='https://gist.githubusercontent.com/curran/a08a1080b88344b0c8a7/raw/0e7a9b0a5d22642a06d3d5b9bcbad9890c8ee534/iris.csv'
    iris = pd.read_csv(url)

    return iris

@app.get("/plot-iris")
def plot_iris():

    import pandas as pd
    import matplotlib.pyplot as plt

    url ='https://gist.githubusercontent.com/curran/a08a1080b88344b0c8a7/raw/0e7a9b0a5d22642a06d3d5b9bcbad9890c8ee534/iris.csv'
    iris = pd.read_csv(url)

    plt.scatter(iris['sepal_length'], iris['sepal_width'])
    plt.savefig('iris.png')
    file = open('iris.png', mode="rb")

    return StreamingResponse(file, media_type="image/png")