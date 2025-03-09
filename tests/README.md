# C2 Platform Tests

This directory contains automated tests for the C2 Platform.

## Test Files

- `frontend_tests.py`: Tests for the public-facing website functionality (early access signup, job applications, contact form)
- `admin_tests.py`: Tests for admin functionality, newsletter signup, and email sending process

## Running the Tests

### Frontend Tests

To run the frontend tests:

```bash
# Activate the virtual environment
source venv/bin/activate

# Run the tests
python tests/frontend_tests.py --base-url "http://localhost:5000" --email "test@example.com"
```

### Admin Tests

To run the admin tests, use the provided script:

```bash
# Run the tests (replace with your admin credentials)
./run_admin_tests.sh "admin@example.com" "your_password"
```

Or run the test file directly:

```bash
# Activate the virtual environment
source venv/bin/activate

# Run the tests
python tests/admin_tests.py --base-url "http://localhost:5000" --admin-email "admin@example.com" --admin-password "your_password"
```