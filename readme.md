My DevOps Learning Project

This is a simple project I built to practice DevOps skills. It is a Python web application that I put inside a Docker container and connected to GitHub Actions for automatic testing.

What I Learned
Docker How to create a Dockerfile and build images.
CI/CD: How to use GitHub Actions to run tests automatically.
Python: Building a basic API with Flask.
Testing: Writing simple unit tests with Pytest.

How to Run It
1.  Build the image:
    docker build -t python-api .
2.  Run the container:
    docker run -p 5000:5000 python-api.