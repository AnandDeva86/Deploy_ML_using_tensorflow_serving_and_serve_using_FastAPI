# RestAPI to serve the deployed model.

## Description

A fastAPI that consume and then serve predictions from the served model deployed using tensorflow/serving.

## Getting Started

### Dependencies 

#### Deployment
* FastAPI
* Tensorflow/serving
* Poetry 
* requests
* uvicorn

#### Unit test
* Pytest

#### Integration test
* selenium
* chromedriver_autoinstaller
#### System test
* Locust


### Deployment Instruction

* Build the docker-compose.yml

```
docker-compose up -d --build

```

* The application runs on the [local host](http://127.0.0.1:8000/docs).
* Pass the required parameters(Cylinders, Displacement, Horsepower, Weight, Acceleration, Model Year, Europe, Japan, USA) in the swagger ui get or post response body.
* Stop the containers using

```
docker-compose down
```

## Authors
[Anand Devarajan](https://www.linkedin.com/in/ananddevarajan)

## Version History
* 0.1
    * Initial Release

## License

see the LICENSE.md file for details