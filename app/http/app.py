from injector import Injector
import dotenv
from internal.router import Router
from internal.server import Http
from config import Config

injector = Injector()
config = Config()
dotenv.load_dotenv()

app = Http(__name__, conf=config, router=injector.get(Router))

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=7001)
