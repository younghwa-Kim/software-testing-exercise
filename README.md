# Software testing hands-on for CS350

## Unit Testing with PyTest
Use `pytest` to test using your test file.
```bash
pytest test_car.py
```
## Coverage
Use `coverage` to find your test coverage metrics.
```bash
coverage run –-branch –m pytest test_car.py
coverage report
```

## Test Generation with Pynguin
Pynguin looks for your code in the current directory and writes out the generated test file in `pynguin-tests` dir. We will use pynguin version `0.40.0`.
```bash
pynguin \
    --project-path ./ \
    --output-path pynguin-tests \
    --module-name car
    -v
```

