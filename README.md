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

# Todos

### Settingshandler
- [x] Create interface that reads settings template json file
- [x] Save settings to settings data file
- [x] Parse settings to make them easier to access from internal software api
- [ ] Add dynamic settings limits feature (limits change based on the capabilites of the current system)
- [ ] Add feature to save configurations

### Logging
- [x] Get logger working.
- [x] Implement logging.
- [x] Create different formatter for file logger.
- [x] Show logs in the UI.
- [x] Implement logs with sockets.
- [x] Create independen log agent which emits sockets events with the logs data every second.

### Internal 
- [x] Make the constants file into an actual class which gets loaded and prepares the data beforehand.
- [x] Create a page and system to handle and start the different servers..
- [ ] Create an interface to see what agents are running for the agentsHandler.
- [ ] Integrate virtual files for logging instead than writing a file every time.

### Vision
- [ ] Create webcam init routine.
- [x] Stream and conver stream to a api endpoint.
- [ ] Implement webcam extender.
- [ ] Miltithread camera class to stream to multiple devices at the same time.
- [ ] Add stream control functionalitites: Pause, Start recording and such.

### Motory system
- [ ] Create fake motory system api for testing.
- [ ] Plan an encoding system for the different commands to send to the mount.
- [ ] Create a webserver for the motory system.
- [ ] Integrate with pilot console.
- [ ] Integrate keyboard input.
- [ ] Integrate planning movements.

### Host Machine UI
- [ ] Create CLI setup system UI for host machine.
