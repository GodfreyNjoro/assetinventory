from flask.cli import FlaskGroup
import os
from catalogue import create_app, db
#from flask_migrate import Migrate

app = create_app(os.getenv('FLASK_CONFIG') or 'default')
#migrate = Migrate(app, db)

cli = FlaskGroup(app)

@cli.command()
def recreate_db():
    db.drop_all()
    db.create_all()
    db.session.commit()

@cli.command()
def test():
    """ run the unit tests """
    import unittest
    tests = unittest.Testloader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)

if __name__ == '__main__':
    cli()