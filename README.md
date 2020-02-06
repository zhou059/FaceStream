# w251 HW3 Spring '20

Wasn't able to get message fowarding between local and cloud broker so I just published directly to the cloud broker. Didn't use alpine containers or mosquitto broker on the Jetson in the end. 

### Setup on IBM Cloud VM first: 

1. Install s3fs
2. echo "QhZHiiAwhZCkX7yHf6S5:KMODLfipNUIiLCfmYEjsg6pbIPDlV2g9iTThKKyQ" > $HOME/.cos_creds
3. chmod 600 $HOME/.cos_creds
4. mkdir /mnt/s3fs_faces
5. s3fs s3fs_faces /mnt/s3fs_faces -o passwd_file=$HOME/.cos_creds -o sigv2 -o use_path_request_style -o url=https://s3.us.cloud-object-storage.appdomain.cloud
6. docker build -t ibmsl_container -f Dockerfile.save .
7. docker run --name mosquitto -p 1883:1883 -v "/root/W251/FaceStream":/FaceStreem -d ibmsl_container mosquitto
8. docker run --name subscriber -v "/root/W251/FaceStream":/FaceStream -v "/mnt/s3fs_faces":/s3fs_faces -ti cloud_ivs bash
python3 /FaceStream/saver.py

### Setup instructions on Jetson after: 

1. docker build -t cv2container -f Dockerfile.capture .
2. xhost + local:root
3. docker run --user=root --env="DISPLAY" -e DISPLAY=$DISPLAY \
--volume="/etc/group:/etc/group:ro" --volume="/etc/passwd:/etc/passwd:ro" --volume="/etc/shadow:/etc/shadow:ro" \
--volume="/etc/sudoers.d:/etc/sudoers.d:ro" --volume="/tmp/.X11-unix:/tmp/.X11-unix:rw" \
--name capture --privileged --network hw3 -v "$PWD":/faces -ti cv2container bash

#### In the container: 
1. cd faces
2. python3 faceCapture.py
