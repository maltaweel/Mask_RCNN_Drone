'''
Created on Mar 27, 2021

@author: maltaweel
'''
import os
from pixellib.instance import instance_segmentation


#path 
pn=os.path.abspath(__file__)
pn=pn.split("src")[0]
path=os.path.join(pn,'kangaroo','images','00012.jpg')
model_path=os.path.join(pn,'model_dir')
weights_path=os.path.join(pn,'weights','mask_rcnn_coco.h5')
output_segmentation=os.path.join(pn,'output_segmentation','segmented.jpg')

#segmentation
instance_seg = instance_segmentation()
instance_seg.load_model(weights_path)
instance_seg.segmentImage(path, show_bboxes = True, output_image_name = output_segmentation)