import vrep
import cv2
import array
import numpy as np
import time
from PIL import Image as I

print('program started')
vrep.simxFinish(-1)
clientID=vrep.simxStart('127.0.0.1',19997,True,True,5000,5)
print ('Connected to remote API server')
r, colorCam = vrep.simxGetObjectHandle(clientID, "kinect_rgb", vrep.simx_opmode_oneshot_wait);
r, leftmotor = vrep.simxGetObjectHandle(clientID, "Pioneer_p3dx_leftMotor", vrep.simx_opmode_oneshot_wait);
r, rightmotor = vrep.simxGetObjectHandle(clientID, "Pioneer_p3dx_rightMotor", vrep.simx_opmode_oneshot_wait);

vrep.simxSetJointTargetVelocity(clientID, leftmotor, 0, vrep.simx_opmode_streaming);
vrep.simxSetJointTargetVelocity(clientID, rightmotor, 0, vrep.simx_opmode_streaming);

r, resolution, image = vrep.simxGetVisionSensorImage(clientID, colorCam, 1, vrep.simx_opmode_streaming);
time.sleep(0.5)

l_speed = 0
r_speed = 0
Posicao = 0
while True:
	r, resolution, image = vrep.simxGetVisionSensorImage(clientID, colorCam, 1, vrep.simx_opmode_buffer);
	mat = np.asarray(image, dtype=np.uint8)
	mat2 = mat.reshape(resolution[1], resolution[0], 1)
	image = cv2.flip(mat2, 0)
	r, thresh = cv2.threshold(image,100,255,cv2.THRESH_BINARY)
	for i in range (thresh.shape[0]):
		if(thresh[240, i]) == 0:
			Posicao = i
			break    
	if Posicao < 280:
		l_speed = 0
		r_speed = 1   
	elif Posicao > 380:
		l_speed = 1
		r_speed = 0
	elif Posicao < 280 | Posicao > 380:
		for i in range (thresh.shape[0]):
			if(thresh[400, i]) == 0:
				Posicao = i
				break    
		if Posicao < 280:
			l_speed = 0
			r_speed = 1
		elif Posicao > 380:
			l_speed = 1
			r_speed = 0
		else:
			l_speed = 3
			r_speed = 3
	else:
		l_speed = 3
		r_speed = 3
	vrep.simxSetJointTargetVelocity(clientID, leftmotor, l_speed, vrep.simx_opmode_streaming);
	vrep.simxSetJointTargetVelocity(clientID, rightmotor, r_speed, vrep.simx_opmode_streaming);
	cv2.imshow("robot camera", thresh)
	cv2.waitKey(1)
