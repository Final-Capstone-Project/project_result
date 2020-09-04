from keras.applications import MobileNetV2
from keras.models import Sequential, Model
from keras.layers import Dense, Dropout, Activation, Flatten, GlobalAveragePooling2D
from keras.optimizers import RMSprop, Adam
from keras.callbacks import ModelCheckpoint, EarlyStopping, ReduceLROnPlateau
from keras.preprocessing.image import ImageDataGenerator
import glob, os.path as osp

# 크기 사이즈
img_rows, img_cols = 224, 224
mobilenet = MobileNetV2(weights='imagenet', include_top=False, input_shape=(img_rows, img_cols, 3))

for layer in mobilenet.layers:
    layer.trainable = True


def addTopModelMobileNet(bottom_model, num_classes):
    """creates the top or head of the model that will be
        placed ontop of the bottom layers"""
    top_model = bottom_model.output
    top_model = GlobalAveragePooling2D()(top_model)
    top_model = Dense(1280, activation='relu')(top_model)
    top_model = Dropout(0.5, top_model)
    top_model = Dense(1280, activation='relu')(top_model)
    top_model = Dropout(0.5, top_model)
    top_model = Dense(512, activation='relu')(top_model)
    top_model = Dense(num_classes, activation='softmax')(top_model)
    return top_model


num_classes = 2
FC_Head = addTopModelMobileNet(mobilenet, num_classes)
model = Model(inputs=mobilenet.input, outputs=FC_Head)
train_data_dir = './data/train'
valid_data_dir = './data/validation'
train_datagen = ImageDataGenerator(
    rescale=1. / 255,
    rotation_range=30,
    width_shift_range=0.3,
    height_shift_range=0.3,
    horizontal_flip=True,
    fill_mode='nearest')
validation_datagen = ImageDataGenerator(rescale=1. / 255)
batch_size = 16
train_path = glob.glob(train_data_dir + '/*')
train_target = [1 if osp.basename(path)[0] == 'f' else 0 for path in train_path]
train_generator = train_datagen.flow_from_directory(
    train_data_dir,
    target_size=(img_rows, img_cols),
    batch_size=batch_size,
    class_mode='categorical',
    classes=['fire', 'non-fire']
)

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
    patience=10,
    verbose=1, restore_best_weights=True)

learning_rate_reduction = ReduceLROnPlateau(monitor='val_acc',
                                            patience=5,
                                            verbose=1,
                                            factor=0.2,
                                            min_lr=0.0001)
callbacks = [earlystop, checkpoint, learning_rate_reduction]
model.compile(loss='categorical_crossentropy',
              optimizer=Adam(lr=0.001),
              metrics=['accuracy'])
nb_train_samples = 100
nb_validation_samples = 30
epochs = 5
history = model.fit_generator(
    train_generator,
    steps_per_epoch=nb_train_samples // batch_size,
    epochs=epochs,
    callbacks=callbacks,
    validation_data=validation_generator,
    validation_steps=nb_validation_samples // batch_size)
