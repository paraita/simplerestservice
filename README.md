# simplerestservice
A dockerized simple REST service that can be used for demo purpose.
The image provides the following APIs:

* wordcounter
* linecounter

To start the `linecounter` services, simply use:

```
docker run --rm -it -p 5000:5000 -e SERVICE=linecounter paraita/simplestrestservice
```
