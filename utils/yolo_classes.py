"""yolo_classes.py

NOTE: Number of YOLO COCO output classes differs from SSD COCO models.
"""

COCO_CLASSES_LIST = [
    'person',
    'man',
    'girl',
    'elder',
    'children',
]

# For translating YOLO class ids (0~79) to SSD class ids (0~90)
yolo_cls_to_ssd = [
    1, 2, 3, 4, 5,
]


def get_cls_dict(category_num):
    """Get the class ID to name translation dictionary."""
    if category_num == 5:
        return {i: n for i, n in enumerate(COCO_CLASSES_LIST)}
    else:
        return {i: 'CLS%d' % i for i in range(category_num)}
