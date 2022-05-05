from tensorflow import keras
import numpy as np
from tensorflow.keras.preprocessing.image import load_img
from sklearn.preprocessing import LabelEncoder
from tensorflow.keras.utils import to_categorical

labelencoder = LabelEncoder()

class BuildingDataset(keras.utils.Sequence):
    """
    Sequence class to load & vectorize batches of data.
    
    Iterate over the data (as Numpy arrays).
    
    Reference - https://keras.io/examples/vision/oxford_pets_image_segmentation/#prepare-sequence-class-to-load-amp-vectorize-batches-of-data
    """

    def __init__(self, batch_size, img_size, input_img_paths, target_img_paths):
        self.batch_size = batch_size
        self.img_size = img_size
        self.input_img_paths = input_img_paths
        self.target_img_paths = target_img_paths

    def __len__(self):
        return len(self.target_img_paths) // self.batch_size

    def __getitem__(self, idx):
        """Returns tuple (input, target) correspond to batch #idx."""
        i = idx * self.batch_size
        batch_input_img_paths = self.input_img_paths[i : i + self.batch_size]
        batch_target_img_paths = self.target_img_paths[i : i + self.batch_size]

        # load images
        x = np.zeros((self.batch_size,) + self.img_size + (2,), dtype="float32")
        for j, path in enumerate(batch_input_img_paths):
            img = tfl.imread(path)
            img[np.where(np.isnan(img))] = 0
            
            img = np.moveaxis(img,0,2)
        

            x[j] = img

        # load masks
        y = np.zeros((self.batch_size,) + self.img_size+ (3,) , dtype="int8")
        for j, path in enumerate(batch_target_img_paths):
            mask = tfl.imread(path)
            # mask[np.where(np.isnan(mask))] = 0
            # # mask[mask == -1 ]= 0
            # mask= np.expand_dims(mask,-1)
            # train_masks_reshaped = mask.reshape(-1,1)
            # train_masks_reshaped_encoded = labelencoder.fit_transform(train_masks_reshaped)
            # train_masks_cat = to_categorical(train_masks_reshaped_encoded, num_classes=3)
            mask[np.where(np.isnan(mask))] = 0
            # mask[mask == -1 ]= 0
            # mask= np.expand_dims(mask,-1)

            train_masks_reshaped = mask.reshape(-1,1)
            train_masks_reshaped_encoded = labelencoder.fit_transform(train_masks_reshaped)
            train_masks_cat = to_categorical(train_masks_reshaped_encoded, num_classes=3)
            train_masks_cat= train_masks_cat.reshape(512,512,3)


            y[j] = train_masks_cat
            # print(np.unique(y[j]))
            
        return x, y