class NumberChecker:
    def __init__(self):
        pass
    def excute(self):
        import numpy as np
        import matplotlib.pyplot as plt
        from tensorflow import keras
        mnist = keras.datasets.mnist
        (train_images,train_labels),(test_images,test_labels) = mnist.load_data()
        #print('훈련이미지: ',train_images.shape)
        #print('훈련 라벨: ', train_labels.shape)
        #print('테스트이미지: ', test_images.shape)
        #print('테스트 라벨: ', test_labels.shape)

        plt.figure(figsize=(5,5))
        image=train_images[100]
        plt.imshow(image)
        plt.show()
