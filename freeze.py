from  import Freezer
from universe import app

freezer = Freezer(app)

if __name__ == '__main__':
    freezer.freeze()