import unittest
from flask_testing import TestCase

from manage import app


class TestDevelopmentConfig(TestCase):
    def create_app(self):
        app.config.from_object('main.config.DevelopmentConfig')
        return app

    def test_app_is_development(self):
        self.assertTrue(app.config['SECRET_KEY'])
        self.assertTrue(app.config['DEBUG'])


class TestTestingConfig(TestCase):
    def create_app(self):
        app.config.from_object('main.config.TestingConfig')
        return app

    def test_app_is_testing(self):
        self.assertTrue(app.config['SECRET_KEY'])
        self.assertTrue(app.config['DEBUG'])
        self.assertTrue(app.config['TESTING'])


class TestProductionConfig(TestCase):
    def create_app(self):
        app.config.from_object('main.config.ProductionConfig')
        return app

    def test_app_is_production(self):
        self.assertFalse(app.config['DEBUG'])


if __name__ == '__main__':
    unittest.main()