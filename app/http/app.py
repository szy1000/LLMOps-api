from injector import Injector
import dotenv
from internal.router import Router
from internal.server import Http

injector = Injector()

dotenv.load_dotenv()

app = Http(__name__, router=injector.get(Router))

if __name__ == "__main__":
    app.run(debug=True)
