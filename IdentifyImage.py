import cv2
import os
file_loc = 'downloads/Popeye/'

# import shutil
# for i, f in enumerate(os.listdir(file_loc)):
#     shutil.move(file_loc+f, file_loc+'{}.jpg'.format(i))
template = cv2.imread(file_loc+'Face.jpg')

for image in os.listdir(file_loc):
    if image == 'Face.jpg':
        continue
    cur_image = cv2.imread(file_loc+image)
    result = cv2.matchTemplate(image=cur_image, templ=template, method=cv2.TM_SQDIFF) # TM_SQDIFF_NORMED
    mn, _, mnLoc, _ = cv2.minMaxLoc(result)
    MPx, MPy = mnLoc
    trows, tcols = template.shape[:2]
    print('MPx, MPy =', MPx, MPy, 'trows, tcols =', trows, tcols)
    cv2.rectangle(cur_image, (MPx, MPy), (MPx + tcols, MPy + trows), (0, 0, 255), 2)
    cv2.imshow('output', cur_image)
    cv2.waitKey(0)




