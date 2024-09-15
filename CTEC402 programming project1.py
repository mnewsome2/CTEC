# Reads data
import numpy as np
import pandas
# Splits data for training and testing
from sklearn.model_selection import train_test_split
# Core model
from tensorflow.keras.models import Sequential
# Builds layers
from tensorflow.keras.layers import Dense, Input, BatchNormalization
# Optimizer
from tensorflow.keras.optimizers import Adam
# Model callback
from tensorflow.keras.callbacks import Callback
# Tells us how accurate our model is
from sklearn.metrics import classification_report, confusion_matrix, precision_recall_fscore_support
# Preprocessor
from sklearn.preprocessing import MinMaxScaler
# Reconstructs data
import numpy
# Plots results
import matplotlib.pyplot as plt


# Custom callback to compute precision, recall, and F1 after each epoch
class MetricsCallback(Callback):
    def __init__(self, x_test, y_test, threshold_percentile):        self.x_test = x_test

    self.y_test = y_test
    self.threshold_percentile = threshold_percentile
    self.precision = []
    self.recall = []
    self.f1 = []


def on_epoch_end(self, epoch, logs=None):
    # Predict using the model at the end of each epoch
    reconstruct = self.model.predict(self.x_test)
    reconstruct_error = np.mean(np.power(self.x_test - reconstruct, 2), axis=1)

    # Define a threshold for anomaly detection
    threshold = np.percentile(reconstruct_error, self.threshold_percentile)
    y_pred = np.array([1 if error > threshold else 0 for error in reconstruct_error])

    # Compute precision, recall, F1
    precision, recall, f1, _ = precision_recall_fscore_support(self.y_test, y_pred, average='binary')

    # Store the metrics
    self.precision.append(precision)
    self.recall.append(recall)
    self.f1.append(f1)


# imports the data
data = pandas.read_csv("synthetic_network_traffic.csv")
# Used for preprocessing
scaler = MinMaxScaler()
# Removes the IsAnomaly column from the dataframe for testing and preprocesses data
x = pandas.get_dummies(data.drop(["IsAnomaly"], axis=1))
x = scaler.fit_transform(x)
# Gets the values from IsAnomaly
y = data["IsAnomaly"].astype(int)
# Uses a random 20% of the data for testing
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=.2, random_state=42)

model = Sequential()
# Builds our neural network layers
model.add(Input(shape=(x_train.shape[1],)))
model.add(Dense(units=128, activation="relu"))
model.add(BatchNormalization())
model.add(Dense(units=64, activation="relu"))
model.add(Dense(units=x_train.shape[1], activation="sigmoid"))
# compiles our model
optimizer = Adam(learning_rate=0.0001)
model.compile(loss="mae", optimizer=optimizer)

# Instantiate the custom metrics callback
metrics_callback = MetricsCallback(x_test, y_test, threshold_percentile=85)

# Begins training model on normal data
normal = x_train[y_train == 0]
history = model.fit(normal, normal, epochs=25, batch_size=32, validation_split=0.2, callbacks=[metrics_callback])

# Plot loss over epochs
plt.figure(figsize=(12, 6))
plt.plot(history.history['loss'], label='Training Loss')
plt.title('Training Loss over Epochs')
plt.xlabel('Epochs')
plt.ylabel('Loss')
plt.legend()
plt.show()

# Tests autoencoder model(Reconstructs data based off of training data to find anomalies)
reconstruct = model.predict(x_test)
reconstruct_error = numpy.mean(numpy.power(x_test - reconstruct, 2), axis=1)
threshold = np.percentile(reconstruct_error, 85)
y_predict = np.array([1 if error > threshold else 0 for error in reconstruct_error])

# Prints Results
print(classification_report(y_test, y_predict))
print(confusion_matrix(y_test, y_predict))

# Save the model to a file
model.save("AnomalyDetection.keras")

