from flask_script import Manager
from todo import app
from todo.scripts.db import InitDB

if __name__ == "__main__":
    manager = Manager(app)
    manager.add_command("init_db", InitDB())
    manager.run()
