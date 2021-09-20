import os
import unittest

from flask_migrate import Migrate, MigrateCommand
from flask_restful import Api
from flask_script import Manager

from app import create_app, db
from main.controllers.shortcut import ShortCutCreate, ShortCutGenerate, ShortCutRedirect

app = create_app(os.getenv('BUILD_ENV'))
app.app_context().push()

api = Api(app)
api.add_resource(ShortCutCreate, '/create')
api.add_resource(ShortCutGenerate, '/generate')
api.add_resource(ShortCutRedirect, '/<path:content>')


manager = Manager(app)
migrate = Migrate(app, db)
manager.add_command('db', MigrateCommand)


@manager.command
def run():
    app.run(host='0.0.0.0', port=8000)


@manager.command
def migrate():
    with app.app_context():
        db.create_all()


@manager.command
def test():
    """Runs the unit tests."""
    tests = unittest.TestLoader().discover('tests', pattern='test*.py')
    result = unittest.TextTestRunner(verbosity=2).run(tests)
    if result.wasSuccessful():
        return 0
    return 1


if __name__ == '__main__':
    manager.run()
