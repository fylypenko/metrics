### Project Title

The script prints CPU and RAM metrics.

### Prerequisites

Install Docker. Please see the [Docker installation documentation](https://docs.docker.com/install/)

Install Git. Please see the [Git documentation](https://git-scm.com/docs)

### Installing, usage

Build docker image
```
docker build https://github.com/fylypenko/metrics.git -t metrics-app
```
Run docker container
```
docker run metrics-app <arg>
```
The script accept a single argument to specify which metrics set to print:

cpu - prints CPU metrics (docker run metrics-app cpu)

mem - prints RAM metrics (docker run metrics-app mem)

## Author

[Dmitriy Fylypenko](https://github.com/fylypenko)
