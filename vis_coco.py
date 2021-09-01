import os
import cv2
from tools import drawRect
from pycocotools.coco import COCO

json_file = r'D:\Dataset\VOC\VOCdevkit\VOC2007\val.json'
dataset_dir = r'D:\Dataset\VOC\VOCdevkit\VOC2007\JPEGImages'
coco = COCO(json_file)
imgIds = coco.getImgIds() # 图片id，许多值

for i in range(len(imgIds)):
    img = coco.loadImgs(imgIds[i])[0]
    print(dataset_dir + img['file_name'])
    img_path = os.path.join(dataset_dir, img['file_name'])
    assert os.path.exists(img_path)
    image = cv2.imread(img_path)
    annIds = coco.getAnnIds(imgIds=img['id'], iscrowd=None)
    annos = coco.loadAnns(annIds)

    bbox_list = []
    for i in range(len(annos)):
        obj_struct = {}
        bbox = annos[i]['bbox']
        x, y, w, h = bbox
        xmin = int(float(x))
        ymin = int(float(y))
        xmax = int(float(x)) + int(float(w))
        ymax = int(float(y)) + int(float(h))
        if (xmin >= xmax) or (ymin >= ymax):
            print("Warning {} , bbox: xmin_{}, ymin_{}, xmax_{}, ymax_{}".format(
                os.path.basename(filename), xmin, ymin, xmax, ymax
            ))
        obj_struct['bbox'] = [xmin, ymin, xmax, ymax]
        obj_struct['name'] = coco.loadCats(annos[i]['category_id'])[0]['name']
        bbox_list.append(obj_struct)

    im_vis = drawRect(image, bbox_list, score=False)

    # 参数为(显示的图片名称，要显示的图片)  必须加上图片名称，不然会报错
    cv2.imshow('demo', im_vis)
    cv2.waitKey(5000)