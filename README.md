# Flood Segmentation using Tensorflow 
Intern Project at GIC : Flood water body segmentation using Unet Structure
Ref : https://github.com/cloudtostreet/Sen1Floods11 ( in Pytorch version )


# Data Structure
|Training |    Label    |  
| --- | --- |
| 'S1 Hand' | 'JRC Water Hand' |
| 'S1 Hand'   | 'Label Hand' |
| 'S1 Hand' | 'S1Otsu Hand' |
| 'S1 Hand' | 'S2 Label' |
| 'S1 Weak' | 'S1Otsu Label Weak' |
| 'S1 Weak' | 'S2Index Label Weak' |
| 'S1 Perm' | 'JRC Perm' |






## Project Structure
The descriptions of principal files in this project are introduced as follows:
* Models            : include model weights,notebooks and predictions
* utils/dataset.py  : tensorflow data loader for loading up images into model
* utils/loss.py     : custom losses for tensorflow such as dice coefficient, bce dice loss
* utils/metrics.py  : metrics for model ( precision,recall, f1 )
* utils/models.py   : include model frames for Unet,DeepUnet
* Notebooks         : include data mounting and baseline models for different dataset


## Principal Environmental Dependencies
* numpy
* pandas
* tensorflow
* matplotlib
* keras
* tifffile
* sklearn

## Model Metrics

<img src="Models/3.Train%20'S1%20Hand'%20Label%20'S1OtsuLabelHand'/3_Train_S1%20Hand_Label_S1_otsu_Hands_Metrics.png" width="500" height="300" > 

## Model Results ( Sample Model using Train ' S1 Hand' Label 'S1OtSuLabel Hand')


| Unet Results |    Traininig In percentage    |    Validation In percentage    |  
| --- | --- | --- |
| precsion | 0.8779 | 0.6666 |
| recall   | 0.8873 | 0.6719 |
| f1_score | 0.8785 | 0.6577 |


## Predicted Results 
<img src="Models/3.Train%20'S1%20Hand'%20Label%20'S1OtsuLabelHand'/Preds_3_Train_S1%20Hand_Label_S1_otsu%20Hand/Preds_0.png" width="500" height="300" > 
<img src="Models/3.Train%20'S1%20Hand'%20Label%20'S1OtsuLabelHand'/Preds_3_Train_S1%20Hand_Label_S1_otsu%20Hand/Preds_1.png" width="500" height="300" > 
<img src="Models/3.Train%20'S1%20Hand'%20Label%20'S1OtsuLabelHand'/Preds_3_Train_S1%20Hand_Label_S1_otsu%20Hand/Preds_2.png" width="500" height="300" > 
