# How to run the negative test locally

Because this test is a proposal for the real codebase, it includes a mock Express app to demonstrate the behavior.

1. Install the required testing dependencies (in the real project): `npm install supertest express jest --save-dev`
2. Run the test: `npx jest authz.test.js`
3. **Expected output:** The test should pass, demonstrating that the API returns a 403 Forbidden when a patient token tries to access doctor-only endpoints.