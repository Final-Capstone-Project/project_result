from keras.applications import MobileNetV2
from keras.models import Sequential, Model
from keras.layers import Dense, Dropout, Activation, Flatten, GlobalAveragePooling2D
from keras.optimizers import RMSprop, Adam, SGD
from keras.callbacks import ModelCheckpoint, EarlyStopping, ReduceLROnPlateau
from keras.preprocessing.image import ImageDataGenerator
import glob, os.path as osp
import tensorflow as tf

# 전역변수
img_rows, img_cols = 224, 224
mobilenet = MobileNetV2(weights='imagenet', include_top=False, input_shape=(img_rows, img_cols, 3))
train_data_dir = './data/train'
valid_data_dir = './data/validation'
num_classes = 2
batch_size = 32

for layer in mobilenet.layers:
    layer.trainable = True


def addTopModelMobileNet(bottom_model, num_classes):
    top_model = bottom_model.output
    top_model = GlobalAveragePooling2D()(top_model)
    top_model = Dense(4096, activation='relu')(top_model)
    top_model = Dropout(0.3)(top_model)
    top_model = Dense(4096, activation='relu')(top_model)
    top_model = Dropout(0.3)(top_model)
    top_model = Dense(2048, activation='relu')(top_model)
    top_model = Dropout(0.5)(top_model)
    top_model = Dense(1024, activation='relu')(top_model)
    top_model = Dropout(0.5)(top_model)
    top_model = Dense(512, activation='relu')(top_model)
    top_model = Dense(num_classes, activation='softmax')(top_model)
    return top_model


FC_Head = addTopModelMobileNet(mobilenet, num_classes)
model = Model(inputs=mobilenet.input, outputs=FC_Head)

train_datagen = ImageDataGenerator(
    rescale=1. / 255,
    rotation_range=30,
    width_shift_range=0.3,
    height_shift_range=0.3,
    zoom_range=[0.5, 0.5],
    horizontal_flip=True,
    fill_mode='nearest')
validation_datagen = ImageDataGenerator(rescale=1. / 255)

train_path = glob.glob(train_data_dir + '/*')

# 학습 데이터
train_generator = train_datagen.flow_from_directory(
    train_data_dir,
    target_size=(img_rows, img_cols),
    batch_size=batch_size,
    class_mode='categorical',
    classes=['fire', 'non-fire']
)
# 검증 데이터
validation_generator = validation_datagen.flow_from_directory(
    valid_data_dir,
    target_size=(img_rows, img_cols),
    batch_size=batch_size,
    class_mode='categorical')

checkpoint = ModelCheckpoint(
    'fire_mobilNet.h5',
    monitor='val_loss',
    mode='min',
    save_best_only=True,
    verbose=1)
earlystop = EarlyStopping(
    monitor='val_loss',
    min_delta=0,
    patience=3,
    verbose=1, restore_best_weights=True)

learning_rate_reduction = ReduceLROnPlateau(monitor='val_accuracy',
                                            patience=5,
                                            verbose=1,
                                            factor=0.2,
                                            min_lr=0.0001)
callbacks = [earlystop, checkpoint, learning_rate_reduction]
# 모델 학습과정 설정
model.compile(loss='categorical_crossentropy',
              optimizer=SGD(lr=0.001, decay=1e-6, momentum=0.9, nesterov=True),
              metrics=['accuracy'])

# 모델 학습
nb_train_samples = 1272
nb_validation_samples = 50
epochs = 7
history = model.fit_generator(
    train_generator,
    steps_per_epoch=nb_train_samples // batch_size,
    epochs=epochs,
    callbacks=callbacks,
    validation_data=validation_generator,
    validation_steps=nb_validation_samples // batch_size)

# 모델 학습 과정 표시하기
import matplotlib.pyplot as plt

fig, loss_ax = plt.subplots()

acc_ax = loss_ax.twinx()

loss_ax.plot(history.history['loss'], 'y', label='train loss')
loss_ax.plot(history.history['val_loss'], 'r', label='val loss')

acc_ax.plot(history.history['accuracy'], 'b', label='train acc')
acc_ax.plot(history.history['val_accuracy'], 'g', label='val acc')

loss_ax.set_xlabel('epoch')
loss_ax.set_ylabel('loss')
acc_ax.set_ylabel('accuray')

loss_ax.legend(loc='upper left')
acc_ax.legend(loc='lower left')

plt.show()
