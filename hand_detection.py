import cv2
import mediapipe as mp
import time

cap = cv2.VideoCapture(0)
cap.set(3,640)
cap.set(4,480)

ctime = 0
ptime = 0

mphands = mp.solutions.face_mesh
hands = mphands.FaceMesh()
mpDraw = mp.solutions.drawing_utils

""" 
static_image_mode=False
max_num_hands=2
min_detection_confidence=0.5
min_tracking_confidence=0.5
"""

while True:
	_,img = cap.read()
	imgrgb = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
	results = hands.process(imgrgb)
	if  results.multi_face_landmarks:
		for lndm in results.multi_face_landmarks:
			
			for id ,lnd in enumerate(lndm.landmark):
				h,w,_=img.shape
				x = int(lnd.x*w)
				y = int(lnd.y*h)
				if id == 0:
					cv2.circle(img,(x,y),15,(255,0,255),cv2.FILLED)
				print(id,x,y)
			mpDraw.draw_landmarks(img,lndm)
	
	ctime = time.time()
	fps = 1/(ctime-ptime)
	ptime = ctime
	cv2.putText(img,str(int(fps)), (20,40), cv2.FONT_HERSHEY_PLAIN, 3, (255,0,255), 3)

	
	cv2.imshow("main",img)
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break
	