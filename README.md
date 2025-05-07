# CTEC Projects Repository

This repository comprises a collection of projects and assignments developed for various CTEC (Computer Technology) courses. The projects encompass a range of topics, including cybersecurity, cryptography, machine learning, and IoT simulations, primarily implemented in Python.

## Table of Contents

* [Overview]
* [Project List]
* [Getting Started]
* [Prerequisites]
* [Usage]
* [Project Repository -]
        -Project Description
        -Project Dependencies
        -Process
* [License]

## Overview

The projects in this repository demonstrate practical applications of theoretical concepts covered in CTEC coursework. They serve as both learning tools and foundational implementations for topics such as:

* Password encryption and decryption
* Caesar cipher implementation
* Naive Bayes classification
* Decision tree algorithms
* Logistic regression analysis
* Deepfake detection mechanisms
* Network monitoring tools
* IoT simulations (e.g., thermostat control, door lock systems)

## Project List

Below is a list of the key projects included in this repository:

1. **CTEC 445 Encrypt and Decrypt a Password**: A script demonstrating basic password encryption and decryption techniques.
2. **My First Caesar Cipher**: An implementation of the Caesar cipher for basic text encryption.
3. **Naive Bayes**: A project showcasing the Naive Bayes classification algorithm.
4. **Decision Tree**: An example of building and utilizing decision tree models for data classification.
5. **Logistic Regression**: A demonstration of logistic regression for predictive analysis.
6. **Deepfake Detection**: A project aimed at identifying deepfake media using machine learning techniques.
7. **Network Monitoring CTEC402**: Tools and scripts for monitoring network activity and performance.
8. **Thermostat IoT Simulation**: A simulation of a smart thermostat system, illustrating IoT concepts.
9. **Door Lock Server and Client Side**: A simulated smart door lock system, including both server and client-side implementations.
10. **Ransomware Logistic Regression**: An analysis of ransomware behavior using logistic regression models.

## Getting Started

To explore or utilize the projects in this repository:

 **Select a project folder**:
   Each project is contained within its respective directory. Navigate to the desired project to view its contents.
   
## Prerequisites
Ensure you have the following installed on your system:

* Python 3.x
* Required Python libraries (as specified in each project's `requirements.txt` or within the script)

To install necessary libraries, you can use pip:
```bash
pip install -r requirements.txt
```
*Note: Not all projects may have a `requirements.txt` file. In such cases, refer to the script for library dependencies.*
## Usage

Each project contains a Python script or a set of scripts demonstrating specific functionalities. To run a script:
```bash
python script_name.py
```
*Replace `script_name.py` with the actual name of the Python file you wish to execute.*

For projects requiring additional setup or specific instructions, refer to any accompanying documentation or comments within the code.
\*For any questions or further information, please contact the repository owner.\*

# CTEC Project Repository

This repository contains various Python-based cybersecurity, IoT, and machine learning projects completed as part of CTEC coursework. Below is a description of each project, its purpose, dependencies, and how it works.

---

## 1. CTEC 445 Encrypt and Decrypt a Password
**Description**: Generates a secure password with at least 10 characters and a minimum of 2 digits.  
**Dependencies**: `random`, `string`  
**Process**: Randomly selects letters and digits to create a password that meets criteria. May include encryption features.

---

## 2. CTEC402 Programming Project 1
**Description**: Machine learning model using TensorFlow to classify a dataset.  
**Dependencies**: `numpy`, `pandas`, `tensorflow`, `scikit-learn`  
**Process**: Loads data, splits into train/test sets, builds a neural network, and evaluates performance.

---

## 3. Deepfake Detection
**Description**: (No content provided) Placeholder for a model to detect deepfakes using AI.  
**Dependencies**: Unknown  
**Process**: Unknown

---

## 4. My First Caesar Cipher
**Description**: Implements the Caesar cipher algorithm for basic encryption.  
**Dependencies**: `random`, `string`  
**Process**: Shifts characters in a message based on a fixed offset.

---

## 5. Ransomware (Ransonware.py)
**Description**: Trains multiple ML models to detect ransomware.  
**Dependencies**: `pandas`, `numpy`, `scikit-learn`  
**Process**: Loads and preprocesses ransomware data, trains Logistic Regression, Decision Trees, and SVM, and evaluates results.

---

## 6. First Cryptography Code
**Description**: Encrypts/decrypts messages using the `cryptography` library's Fernet module.  
**Dependencies**: `cryptography`  
**Process**: Generates a key, encrypts a message, and decrypts it securely.

---

## 7. Door Lock Client Side
**Description**: Encrypts lock/unlock commands using RSA and sends to a server.  
**Dependencies**: `pycryptodome`, `socket`, `base64`  
**Process**: Loads a public key, encrypts user commands, and sends them over a socket.

---

## 8. Door Lock Server Side
**Description**: Receives encrypted commands and decrypts them using a private RSA key.  
**Dependencies**: `pycryptodome`, `socket`, `base64`  
**Process**: Decrypts commands and executes appropriate door actions.

---

## 9. Thermostat IoT Simulation
**Description**: Simulates encryption performance in IoT thermostats.  
**Dependencies**: `pandas`, `matplotlib`  
**Process**: Evaluates latency, energy use, and throughput across AES, MQTT/TLS, etc.

---

## 10. Logistics Regression
**Description**: Classifies real vs fake images using logistic regression.  
**Dependencies**: `scikit-learn`, `tensorflow`, `matplotlib`  
**Process**: Loads image data, processes features, and trains logistic regression.

---

## 11. Network Monitoring CTEC402
**Description**: Monitors network traffic using Scapy and classifies anomalies with Random Forest.  
**Dependencies**: `scapy`, `networkx`, `matplotlib`, `scikit-learn`  
**Process**: Sniffs packets, extracts features, and classifies data.

---

## 12. Network Monitor CTEC402v3
**Description**: Tracks system network usage and plots the data.  
**Dependencies**: `psutil`, `matplotlib`  
**Process**: Uses psutil to gather real-time network stats and visualizes usage.

---

## 13. Naive Bayes
**Description**: Uses Naive Bayes to classify image data as real or fake.  
**Dependencies**: `scikit-learn`, `tensorflow`, `matplotlib`  
**Process**: Loads and processes images, then applies GaussianNB classifier.

---

## 14. Decision Tree
**Description**: Image classification using a decision tree model.  
**Dependencies**: `scikit-learn`, `tensorflow`, `matplotlib`  
**Process**: Trains a DecisionTreeClassifier on real/fake image data.

---

## 15. Ransomware Logistic Regression
**Description**: ML model for ransomware detection using logistic regression.  
**Dependencies**: `pandas`, `numpy`, `scikit-learn`  
**Process**: Balances data, trains logistic regression, and evaluates the model.

---
