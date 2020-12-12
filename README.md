# TVG Telescope Virtual Guider

A web-tool that allows real-time control of your telescope mount. It also allows path correction ad path planning.
It can show enhanced real-time video feed thanks to the Webcam Extender Core. https://www.youtube.com/watch?v=MOvJCfLYAw8&t=4s

## Technologies
Technologies in terms of hardware and software used by this project.

### Hardware

The project is meant to run on a Raspberry Pi (Pi 4 is hereby recomended) and eventually on a external processing unit(whatever computer that can run a client based on sockets).

### Software

The language used for this proget is Python, and the web interface and API will be coded in flask. 
The GPIO librafy for python will be used to handle the mount.
