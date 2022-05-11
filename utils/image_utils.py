import numpy as np
import tensorflow as tf
import cv2 as cv2
import PIL
from PIL import Image, ImageOps
import os
import gdal
import tifffile as tif

def pad(save_dir,src_img, model_input_w, model_input_h):
    """
    Add extra black area to image to make it ready for cropping
    
    arguments:
        save_dir (Directory) : Directory to store your padded image
        src_img (PIL (or) np array): image to be padded
        model_input_w (int): input image width for model   
        model_input_h (int): input image height for model
    
    returns:
        PIL image: padded image
    """
    
    img_type = type(src_img)

    # change to numpy array
    if img_type  == np.ndarray : 
        img = src_img.copy()
    else: 
        img = np.array(src_img)
    
    img_width = img.shape[1]
    img_height = img.shape[0]
    
    pad_width = int((np.ceil(img_width / model_input_w) * model_input_w) - img_width)
    pad_height = int((np.ceil(img_height / model_input_h) * model_input_h) - img_height)
    
    print('image width = ', img_width, ', image height = ', img_height)
    print('pad width = ', pad_width, ', pad height = ', pad_height)
    
    result_image = cv2.copyMakeBorder( img, 0, pad_height, 0, pad_width, cv2.BORDER_CONSTANT)
    os.makedirs(save_dir,exist_ok= True)
    print('Padded Image shape',result_image.shape)
    tif.imwrite(str(save_dir)+'padded_image.tif',result_image)
    
    return result_image

def crop( gdal_dataset,model_input_w ,model_input_h ,save_dir):
    """
      gdal_dataset : read the tifffile using gdal.Open and pass it to gdal_dataset
      model_input_w : width of model input
      model_input_h : height of model input
      save_dir : Directory to store data


    """
    ds = gdal_dataset
    # ds = gdal.Open('/content/padded_img.tif')
    print(ds.ReadAsArray().shape)
    img_height = ds.ReadAsArray().shape[2]
    img_width  = ds.ReadAsArray().shape[1]

    os.makedirs(save_dir,exist_ok = True )

    box_list =[]
    arr = []
    for i in range(img_height//model_input_h):
        # hori = []
        for j in range(img_width//model_input_w):
            box = [j*model_input_w, i*model_input_h, 512,512]
            print("coordinates",box[:2])
            box_list.append(box[:2])
            # gdal.Translate('/content/cropped_images/cropped_images_'+str(i)+'_'+str(j)+'.tif',ds,srcWin=box)
            gdal.Translate(str(save_dir)+'cropped_images_'+str(i)+'_'+str(j)+'.tif',ds,srcWin=box)
            arr.append(str(save_dir)+'cropped_images_'+str(i)+'_'+str(j)+'.tif')

        
    
  
    return arr,box_list




def reconstruct(preds,img_height,img_width,model_input_h,model_input_w,box_list,numpy=False):
  pred_list = list(preds)

  tiles_list = [Image.fromarray(i, 'L') for i in pred_list]

  first_image = tiles_list[0]

  num_row = int(np.ceil(img_height / model_input_h))
  num_col = int(np.ceil(img_width / model_input_w))

  print(num_row,num_col)



  # create a blank sheet
  contact_sheet=PIL.Image.new(first_image.mode, (first_image.width * num_col,first_image.height * num_row))
  x, y = 0, 0
  for img,j in zip(tiles_list,box_list):
    # print(img,j)
    # paste a single tile in sheet
    contact_sheet.paste(img, j )
    # calculate next position
    if x+first_image.width == contact_sheet.width:
        x=0
        y=y+first_image.height
    else:
        x=x+first_image.width
  # remove extra padded area
  crop_box = (0, 0, 6666,7101)
  print(crop_box)
  new_img = contact_sheet.crop(crop_box)

  if numpy == True:
    new_img = np.array(new_img)



  return new_img
