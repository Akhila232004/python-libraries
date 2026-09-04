![Python Tinitiate Image](../../python_tinitiate.png)

# Python Tutorial
&copy; TINITIATE.COM

##### [Back To Contents](../../README.md)

# Unittest
Software grows in complexity. Bugs creep in when you refactor, upgrade dependencies, or add new features.  

**Unit testing ensures:**
* Code correctness  
* Regression protection (old features don’t break)  
* Confidence in refactoring  
* Automation in CI/CD pipelines  

`unittest` is Python’s standard unit testing framework following the **xUnit family** (similar to JUnit, NUnit). It ships with Python, supports automatic discovery, rich assertions, fixtures, mocking, and integrates with CI and coverage tools.

**Why Testing Matters:**

* **Reliability**: Tests confirm that your functions produce expected outputs.  
* **Safety in Refactoring**: You can modify code with confidence, knowing tests will catch regressions.  
* **Automation**: Tests run automatically in CI/CD pipelines, preventing broken code from being deployed.  
* **Documentation**: Well-written tests serve as examples for how to use your code.

## Installing & Version Notes
* **No installation required**: `unittest` is in the standard library.
* **Version Features**:  
  - Python ≥3.3 includes `unittest.mock`.  
  - Python ≥3.8 introduces `IsolatedAsyncioTestCase` for async testing.  
* **Compatibility**: If you’re working with legacy versions, the `mock` package can be installed separately.
* **Checking Python Version** is important before relying on new features.
```bash
python -V
```

## Your First Test
- **Goal**: Demonstrate the core flow — write a function, write a test, run it.  
- **Principle**: A test case (`TestCase`) groups related tests into a class.  
- **Execution**: `unittest.main()` automatically discovers and runs methods starting with `test_`.  
- **Value**: Even this tiny example shows how to guard against regressions early.  

Let’s build a simple **calculator module** and test it.
```python
# calculator.py
def add(a, b):
    return a + b

def divide(a, b):
    if b == 0:
        raise ValueError("Division by zero")
    return a / b
```
```python
# test_calculator.py
import unittest
import calculator

class TestCalculator(unittest.TestCase):

    def test_add(self):
        self.assertEqual(calculator.add(2, 3), 5)

    def test_divide(self):
        self.assertEqual(calculator.divide(10, 2), 5)

    def test_divide_by_zero(self):
        with self.assertRaises(ValueError):
            calculator.divide(10, 0)

if __name__ == "__main__":
    unittest.main()
```
Run the test:
```bash
python test_calculator.py
```

## Running Tests (CLI & Programmatic)
* **CLI Approach**: `python -m unittest` is the simplest and most common way.  
* **Verbosity**: Add `-v` to see each test case name, useful when debugging.  
* **Programmatic Execution**: Gives more control (e.g., integrating tests into custom scripts).  
* **Discovery**: The discovery mechanism allows you to test large projects without running files manually.  
### CLI (recommended)
* Run all tests discovered under current directory:
```bash
python -m unittest
```
```bash
# Verbose output:
python -m unittest -v
```
### Programmatic
* Run all tests discovered under current directory:
```python
import unittest

suite = unittest.defaultTestLoader.discover(".")
runner = unittest.TextTestRunner(verbosity=2)
runner.run(suite)
```

## Test Discovery & Project Layout
* **Discovery Rule**: By default, `unittest` finds any file named `test*.py` is considered a test file in your project.
* **Structure**: Keeping tests inside a `tests/` folder helps separation and clarity.  
* **Scalability**: This structure supports large projects with multiple modules.  
* **Integration**: Works seamlessly with CI systems that expect a standard layout.  

Typical structure:
```text
project/
├── calculator.py
├── tests/
│   ├── __init__.py
│   ├── test_calculator.py
│   └── test_more.py
```
Run with discovery:
```bash
python -m unittest discover -s tests -p "test_*.py"
```

## Assertions
* Assertions are methods that check expected vs. actual outcomes.  
* They allow you to test equality, membership, type, exceptions, floating-point approximations, etc.  
* When an assertion fails, it produces a clear message indicating what went wrong.  
* Use the most specific assertion available (e.g., `assertIn` instead of `assertTrue(x in y)`).  
    - `assertEqual(a, b)`
    - `assertNotEqual(a, b)`
    - `assertTrue(x)`
    - `assertFalse(x)`
    - `assertIs(a, b)` / `assertIsNot`
    - `assertIsNone(x)` / `assertIsNotNone`
    - `assertIn(a, b)` / `assertNotIn`
    - `assertIsInstance(a, cls)`
    - `assertRaises(exc, func, *args, **kw)`
    - `assertAlmostEqual(a, b, places=7)`
```python
self.assertEqual(2 + 2, 4)
self.assertNotEqual(5, 6)
self.assertTrue(3 < 4)
self.assertFalse("x" in ["a", "b"])
self.assertIsNone(None)
self.assertIsInstance(5, int)
self.assertIn("py", "python")
self.assertAlmostEqual(0.1 + 0.2, 0.3, places=7)
```
**Real-world:** testing JSON response
```python
data = {"id": 1, "name": "Alice"}
self.assertIn("name", data)
self.assertEqual(data["name"], "Alice")
```

## Test Fixtures
* Fixtures prepare and clean up state before and after tests.  
* **Levels**:  
  - `setUp` / `tearDown`: run before/after each test method.  
  - `setUpClass` / `tearDownClass`: run once per test class.  
  - `setUpModule` / `tearDownModule`: run once per test module.  
* Fixtures ensures repeatability and independence of tests.  
* Useful for connecting to databases, opening files, preparing test doubles.  
### Instance-level (`setUp` / `tearDown`)
```python
class TestExample(unittest.TestCase):
    def setUp(self):
        self.data = [1, 2, 3]

    def tearDown(self):
        self.data = None

    def test_sum(self):
        self.assertEqual(sum(self.data), 6)
```
### Class-level (`setUpClass` / `tearDownClass`)
```python
class TestClass(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.resource = open("tmp.txt", "w")

    @classmethod
    def tearDownClass(cls):
        cls.resource.close()
```
### Module-level (`setUpModule` / `tearDownModule`)
```python
def setUpModule():
    print("Before any tests in this module")

def tearDownModule():
    print("After all tests in this module")
```

## Isolating Tests
* **Problem**: Tests should not depend on each other, shared state can lead to flaky, order-dependent tests.  
* **Solution**:  
  - Use `tempfile` for file tests (instead of actual filesystem paths).  
  - Use `unittest.mock.patch.dict` to isolate environment variables, mock environment variables to simulate different setups.  
  - Use `freezegun` (external) or patch `datetime` for time, patch time or randomness for deterministic behavior.  
* **Outcome**: Each test can run in isolation and produce consistent results.
```python
import tempfile, os, unittest

class TestTemp(unittest.TestCase):
    def test_tempfile(self):
        with tempfile.NamedTemporaryFile(delete=False) as f:
            f.write(b"hello")
        self.assertTrue(os.path.exists(f.name))
```

## Subtests
* Sometimes you need to test the same logic with multiple inputs.  
* Writing separate tests leads to duplication.  
* **`subTest` Approach**: Loops with `subTest` let you test multiple cases within one method.  
* If one case fails, the others continue to run, giving a complete picture. Useful for **parameterized / table-driven** testing.
```python
class TestEven(unittest.TestCase):
    def test_even_numbers(self):
        for x in [0, 2, 4, 5, 7]:
            with self.subTest(x=x):
                self.assertEqual(x % 2, 0)
# Output will show which cases failed without stopping the loop.
```

## Skipping & Expected Failures
- **Skipping**: Temporarily disable tests (e.g., when feature not implemented, or OS-specific).  
- **Conditional Skips**: Skip based on runtime conditions like platform or library availability.  
- **Expected Failures**: Mark tests as known failures without breaking the suite.  
- **Use Case**: Useful in agile development where work-in-progress features are under test.  
```python
import sys

class TestSkip(unittest.TestCase):
    @unittest.skip("not ready yet")
    def test_todo(self): pass

    @unittest.skipIf(sys.platform == "win32", "not for Windows")
    def test_linux_only(self): pass

    @unittest.expectedFailure
    def test_known_bug(self):
        self.assertEqual(1, 0)
```

## Grouping Tests: Suites & Loaders
* Sometimes you want fine-grained control over which tests to run.  
* **Test Suites**: Allow you to manually group related test cases.  
* **Test Loaders**: Dynamically discover and add tests to suites.  
* **Use Case**: Running only “fast” tests in development, but the full suite in CI.  
```python
def suite():
    suite = unittest.TestSuite()
    suite.addTest(TestCalculator("test_add"))
    suite.addTest(TestCalculator("test_divide"))
    return suite

if __name__ == "__main__":
    runner = unittest.TextTestRunner()
    runner.run(suite())
```

## Mocking with `unittest.mock`
* Mocking replaces real objects with controlled fake versions.  
* Prevents reliance on slow, fragile, or unavailable dependencies (APIs, DBs, files).  
* **Features**:  
  - Replace functions/classes with `patch`.  
  - Configure return values and side effects.  
  - Assert calls were made with expected arguments.  
* Enables isolated and reliable unit testing.  
```python
from unittest.mock import patch
import requests

@patch("requests.get")
def test_api(mock_get):
    mock_get.return_value.status_code = 200
    resp = requests.get("http://example.com")
    assert resp.status_code == 200
```
**Real-world:** mocking DB connection
```python
@patch("sqlite3.connect")
def test_db(mock_conn):
    mock_conn.return_value.cursor.return_value.fetchone.return_value = (1,)
    conn = sqlite3.connect("dummy")
    cur = conn.cursor()
    assert cur.fetchone()[0] == 1
```

## Testing Exceptions, Warnings, and Logging
* **Exceptions**: `assertRaises` ensures the right error is thrown.  
* **Warnings**: Can capture and assert warnings, ensuring deprecated paths are caught.  
* **Logs**: `assertLogs` verifies that proper logging is done, useful in auditing or monitoring scenarios.  
* **Why Important**: Robust code isn’t just about outputs, but also about side effects like error reporting.  
```python
with self.assertRaises(ValueError):
    int("NaN")
```
**Logs:**
```python
with self.assertLogs("app", level="INFO") as cm:
    logging.getLogger("app").info("User created")
self.assertIn("User created", cm.output[0])
```

## Asynchronous Tests
* Async functions (`async def`) cannot be tested with normal test methods.  
* `IsolatedAsyncioTestCase` provides an event loop per test case.  
* Ensures async logic (network calls, coroutines) is properly validated.  
* Useful in modern apps with async APIs, microservices, or async DB drivers.  
```python
import unittest, asyncio

class TestAsync(unittest.IsolatedAsyncioTestCase):
    async def test_async_add(self):
        async def add(a, b): return a + b
        self.assertEqual(await add(2, 3), 5)
```

## Measuring Coverage
* Code coverage measures how much of your code is executed by tests.  
* `coverage.py` integrates seamlessly with `unittest`.  
* Provides line coverage, branch coverage, and missing lines.  
* Aim for high coverage, but focus on *critical paths* instead of blindly chasing 100%.
```bash
# To install 'coverage' run the following command
python -m pip install coverage
```
```bash
# To run 'coverage', run the following command
coverage run -m unittest
coverage report -m
```

## Continuous Integration Example (GitHub Actions)
* **Why CI?**: Ensures tests are run automatically on every push/PR.  
* **GitHub Actions**: Provides a simple YAML-based workflow.  
* **Integration**: Run `unittest` + coverage reporting in the pipeline.  
* **Outcome**: No code gets merged without passing tests.  
* **Sample workflow:** `.github/workflows/python-tests.yml`
```yaml
name: Python Tests
on: [push, pull_request]
jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - uses: actions/setup-python@v4
        with: { python-version: "3.11" }
      - run: pip install -r requirements.txt
      - run: python -m unittest discover -v
```

## Debugging Failing Tests
* **First Failure**: Use `-f` to stop after the first failure for quicker feedback.  
```bash
python -m unittest -f
```
* **Interactive Debugging**: Use `-m pdb` to drop into Python’s debugger at failure points.  
```bash
python -m unittest -m pdb
```
* **Logging Failures**: Verbose mode (`-v`) shows exactly which test failed and why.  
* **Best Practice**: Debug locally with pdb, fix, rerun — then commit.  

## Best Practices
* Write **small, isolated, deterministic** tests.  
* Prefer **descriptive names** (`test_user_registration_valid_input`).  
* Mock **external dependencies** (network, DB).  
* Automate testing in CI/CD pipelines.  
* Keep tests alongside code but in a dedicated folder for clarity.  

## Ready-to-Use Project Template
* Keep application and tests separate for clarity.  
* Place CI/CD configuration at the root for visibility.  
* Use `requirements.txt` (or `pyproject.toml`) to capture dependencies.  
```text
myproject/
├── mylib/
│   ├── __init__.py
│   └── core.py
├── tests/
│   ├── __init__.py
│   ├── test_core.py
│   └── test_integration.py
├── requirements.txt
└── .github/workflows/python-tests.yml
```

##### [Back To Contents](../../README.md)
***
| &copy; TINITIATE.COM |
|----------------------|
