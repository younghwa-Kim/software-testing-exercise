# Software testing hands-on for CS350

## Unit Testing with PyTest

## Coverage

## Test Generation with Pynguin
Pynguin looks for your code in the current directory and writes out the generated test file in `pynguin-tests` dir. We will use pynguin version `0.40.0`.
```python
$ pynguin \
    --project-path ./ \
    --output-path pynguin-tests \
    --module-name car
    -v
```

