# How to run the negative test locally

Because this test is a proposal for the real codebase, it includes a mock Express app to demonstrate the behavior.

1. Install the required testing dependencies (in the real project):

   ```bash
   npm install supertest express jest --save-dev
   ```

2. Run the test:

   ```bash
   npx jest authz.test.js
   ```

3. **Expected output:**

   The test should pass, demonstrating that the API returns a `403 Forbidden` when a patient token tries to access doctor-only endpoints.

## Local Execution Output

```text
PASS  ./authz.test.js
  Negative Authorization Test
    √ should return 403 Forbidden when trying to access medical vitals without doctor role (56 ms)

Test Suites: 1 passed, 1 total
Tests:       1 passed, 1 total
Snapshots:   0 total
Time:        0.981 s
Ran all test suites matching authz.test.js.
```

## YAML Validation

The `security.yml` workflow file was validated successfully using [YAMLLint.com](https://www.yamllint.com/).

The result was: **Valid YAML!**
