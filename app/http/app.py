import dotenv
# from flask_sqlalchemy import SQLAlchemy
from pkg.sqlalchemy import SQLAlchemy
from injector import Injector

from internal.router import Router
from internal.server import Http
from config import Config
from .module import ExtensionModule

dotenv.load_dotenv()

config = Config()

injector = Injector([ExtensionModule])

app = Http(__name__, conf=config, db=injector.get(SQLAlchemy), router=injector.get(Router))

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=7001)
