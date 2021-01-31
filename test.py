try:
    from run import app
    import unittest
except Exception as e:
    print('some modules are missing' + e)


class FlaskTest(unittest.TestCase):
    # check for response 200
    def test_index(self):
        tester = app.test_client(self)
        response = tester.get("/")
        statusCode = response.status_code
        self.assertEqual(statusCode, 200)

    # check for content (str)
    def test_index_content(self):
        tester = app.test_client(self)
        response = tester.get("/")

        self.assertEqual(response.content_type, 'application/str')


if __name__ == '__main__':
    unittest.main()
