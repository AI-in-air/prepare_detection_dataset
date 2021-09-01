# pycocotools 接口

```python
# The following API functions are defined:
#  COCO       - COCO api class that loads COCO annotation file and prepare data structures.
#  decodeMask - Decode binary mask M encoded via run-length encoding.
#  encodeMask - Encode binary mask M using run-length encoding.
#  getAnnIds  - Get ann ids that satisfy given filter conditions.
#  getCatIds  - Get cat ids that satisfy given filter conditions.
#  getImgIds  - Get img ids that satisfy given filter conditions.
#  loadAnns   - Load anns with the specified ids.
#  loadCats   - Load cats with the specified ids.
#  loadImgs   - Load imgs with the specified ids.
#  annToMask  - Convert segmentation in an annotation to binary mask.
#  showAnns   - Display the specified annotations.
#  loadRes    - Load algorithm results and create API for accessing them.
#  download   - Download COCO images from mscoco.org server.
```



### initialize COCO api for instance annotations

```python
annFile = 'xxx.json'
coco=COCO(annFile)
```



### 利用getCatIds函数获取某个类别对应的ID
```python
ids = coco.getCatIds('person')[0]
print(f'"person" 对应的序号: {ids}')
```



### 利用loadCats获取序号对应的类别
```python
cats = coco.loadCats(1)
print(f'"1" 对应的类别名称: {cats}')
```



### 利用loadCats获取序号对应的类别

```python
cats = coco.loadCats(1)
print(f'"1" 对应的类别名称: {cats}')
```



### 获取满足特定条件的图片（交集）

```python
# 获取包含person的所有图片
imgIds = coco.getImgIds(catIds=[1])
print(f'包含person的图片共有：{len(imgIds)}张')
'''包含person的图片共有：2693张'''
```



### 获取某一类的所有图片

```python
# 获取包含dog的所有图片
id = coco.getCatIds(['dog'])[0]
imgIds = coco.catToImgs[id]
print(f'包含dog的图片共有：{len(imgIds)}张, 分别是：')
print(imgIds)
'''
包含dog的图片共有：218张, 分别是：
[289343, 61471, 472375, 520301, 579321, 494869, 554002, 78823, 419974, 404484, 329219, 68078, 170893, 65485, 498286, 424162, 61108, 67213, 365207, 
'''
```



### 获取某一张图片的信息

```python
imgInfo = coco.loadImgs(imgId)[0]
print(f'图像{imgId}的信息如下：\n{imgInfo}')
'''
图像329219的信息如下：
{‘license’: 1, ‘file_name’: ‘000000329219.jpg’, ‘coco_url’: ‘http://images.cocodataset.org/val2017/000000329219.jpg’,
‘height’: 427, ‘width’: 640, ‘date_captured’: ‘2013-11-14 19:21:56’,
‘flickr_url’: ‘http://farm9.staticflickr.com/8104/8505307842_465524a6a6_z.jpg’,
‘id’: 329219}
'''
```



### 获取该图像对应的anns的Id

```python
# 获取该图像对应的anns的Id
annIds = coco.getAnnIds(imgIds=imgInfo['id'])
print(f'图像{imgInfo["id"]}包含{len(anns)}个ann对象，分别是:\n{annIds}')
anns = coco.loadAnns(annIds)
coco.showAnns(anns)
'''
图像329219包含21个ann对象，分别是:
[8032, 192816, 693180, 1508387, 1510882, 1518236, 1527016, 1529043, 1882305, 1885153, 1885350, 1885410, 1886212, 1886466, 1887489, 1981518, 2106278, 2183575, 2183858, 2213662, 2213709]
'''
```

