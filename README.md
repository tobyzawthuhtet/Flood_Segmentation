# Flood Segmentation using Tensorflow 
Intern Project at GIC : Flood water body segmentation using Unet Structure
Ref : https://github.com/cloudtostreet/Sen1Floods11 ( in Pytorch version )

## Project Structure
The descriptions of principal files in this project are introduced as follows:
* Preds             : include predictions from Unet Model 
* Sample            : websites and pdf resources
* utils/dataset.py  : tensorflow data loader for loading up images into model
* utils/loss.py     : custom losses for tensorflow such as dice coefficient, bce dice loss
* utils/metrics.py  : metrics for model ( precision,recall, f1 )
* utils/models.py   : include model frames for Unet,DeepUnet
* 1_Flood_Mapping_Tensorflow.ipynb : Training Notebook


## Principal Environmental Dependencies
* numpy
* pandas
* tensorflow
* matplotlib
* keras
* tifffile
* sklearn

## Model Metrics

<img src="loss.png" width="500" height="300" > 

## Model Results 


| Unet Results |    In percentage    |
| --- | --- |
| precsion | 72.02844619750977|
| f1_score | 73.25286865234375 |
| recall   | 74.87762570381165 |


## Predicted Results 
<img src="/Preds/Preds_4.png" width="500" height="300" > 
<img src="/Preds/Preds_5.png" width="500" height="300" > 
<img src="/Preds/Preds_6.png" width="500" height="300" > 
