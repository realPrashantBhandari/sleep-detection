# sleep-detection
The use case of this program was to detect if a driver is sleeping on the wheel or not. The script uses dlib and opencv libraries.

# Working

The programs calculate the ratio of the vertical and horizontal distance in a persons eye. If this ration is less than a certain number the program determines that the eye is closed.
If the eyse is closed, a startTimer will start ticking the the elapsed time the eye has been close. If this timer goes over 5 sec, the person is determined to be sleeping.

Another parameter to determine the sleep is the head tilt. If the tilt angle is less than 35 degrees the timer will start. If the timer reaches the upper limit (5 sec) the person is considered sleeping.

# Requirements
  1. install python 3.6 in your environment
  2. install open cv  using the follwoing command - pip install opencv-python
  3. install dlib by going to the following link - https://pypi.org/simple/dlib/ 
     then right click the version that meets your requirements and select copy link address
     open cmd on your system and tyle the following command - python -m pip install Past_link_here
     (the final command should look like this python -m pip install https://files.pythonhosted.org/packages/0e/ce/f8a3cff33ac03a8219768f0694c5d703c8e037e6aba2e865f9bae22ed63c/dlib-19.8.1-cp36-cp36m-win_amd64.whl#sha256=794994fa2c54e7776659fddb148363a5556468a6d5d46be8dad311722d54bfcf )
     
  4. copy the shape_predictor_68_face_landmarks.dat file in your working library
  
# You are done, Enjoy !!
