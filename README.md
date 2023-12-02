# SoCoA03
Software construction assignment 3

## Test coverage ## 
## Test Coverage

To measure the test coverage, we use `pytest` along with `coverage.py`. 

1. Install the required packages:
    
    pip install pytest coverage

2. Run the tests with coverage:

    coverage run -m pytest + file.py

3. Generate a coverage report:

    - For a terminal report:

        coverage report
  
    - For a detailed HTML report:

        coverage html

The HTML report will be in the `htmlcov` directory, open `htmlcov/index.html` in the browser to view it.
