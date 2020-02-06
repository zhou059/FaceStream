# w251 HW3 Spring '20

Wasn't able to get message fowarding between local and cloud broker so I just published directly to the cloud broker. Didn't use alpine containers or mosquitto broker on the Jetson in the end. 

### Setup on IBM Cloud VM first: 

1. 

### Setup instructions on Jetson after: 

1. docker build --network=host -t cv2container -f Dockerfile.capture .
2. xhost + local:root
3. docker run --user=root --env="DISPLAY" -e DISPLAY=$DISPLAY \
--volume="/etc/group:/etc/group:ro" --volume="/etc/passwd:/etc/passwd:ro" --volume="/etc/shadow:/etc/shadow:ro" \
--volume="/etc/sudoers.d:/etc/sudoers.d:ro" --volume="/tmp/.X11-unix:/tmp/.X11-unix:rw" \
--name capture --privileged --network hw3 -v "$PWD":/faces -ti cv2container bash

#### In the container: 
1. cd faces
2. python3 faceCapture.py
