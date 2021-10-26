import sys
import base64
import cv2
import numpy as np
import io

data = open(sys.argv[1], 'rb').read()
encoded = base64.b64encode(data).decode('utf-8')
print(encoded)

decoded = base64.b64decode(encoded)
png = np.frombuffer(decoded,dtype=np.uint8)
img = cv2.imdecode(png, cv2.IMREAD_COLOR)
cv2.imwrite(sys.argv[1] ,img)
