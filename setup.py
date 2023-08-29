from setuptools import setup, find_packages

setup(name="automationexercise",
      version="1.0",
      description="Practice API testing",
      author="Luis González",
      packages=find_packages(),
      zip_safe=False,
      install_requires=[
          "Faker==19.3.0",
          "jsonschema==4.19.0",
          "pytest==7.1.3",
          "pytest-html==2.1.1",
          "requests==2.23.0",
          "python-dotenv==1.0.0",
          "PyMySQL==0.9.3"
      ]
      )
