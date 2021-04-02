'''
Created on Apr 2, 2021

@author: maltaweel
'''
import os
import pixellib
from pixellib.instance import custom_segmentation

#path 
pn=os.path.abspath(__file__)
pn=pn.split("src")[0]
path=os.path.join(pn,'Nature','test','butterfly (100).jpg')
model_path=os.path.join(pn,'model_dir')
weights_path=os.path.join(pn,'weights','mask_rcnn_model.002-0.941997.h5')
output_segmentation=os.path.join(pn,'output_segmentation','segmented.jpg')

#segment
segment_image = custom_segmentation()
segment_image.inferConfig(num_classes= 2, class_names= ["BG", "butterfly", "squirrel"])
segment_image.load_model(weights_path)
segment_image.segmentImage(path, show_bboxes=True, output_image_name=output_segmentation,
extract_segmented_objects= True, save_extracted_objects=True)