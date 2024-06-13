# SMS Spam Detection

## Overview

This project implements a machine learning model for detecting spam SMS messages. The model distinguishes between legitimate ("ham") and spam messages based on a dataset of labeled SMS texts.

## Dataset

The SMS Spam Collection dataset consists of 5,574 SMS messages in English, sourced from various public and research-oriented sources:

- **Grumbletext Web site**: 425 SMS spam messages.
- **NUS SMS Corpus (NSC)**: 3,375 randomly chosen ham messages.
- **Caroline Tag's PhD Thesis**: 450 SMS ham messages.
- **SMS Spam Corpus v.0.1 Big**: 1,002 ham messages and 322 spam messages.

## Project Structure

The project is structured as follows:

- `train_model.ipynb`: Jupyter notebook for data preprocessing, model training, and saving the model.
- `streamlit_app.py`: Streamlit application for deploying the trained model.
- `vectorizer.pkl`: Pickle file containing the TF-IDF vectorizer used to preprocess text data.
- `model.pkl`: Pickle file containing the trained machine learning model for SMS spam detection.
- `requirements.txt`: List of Python packages required to run the project.

## Requirements

- Python 3.7+
- Required Python packages are listed in `requirements.txt`.

## Instruction To Run
- First Flok the Repo
- Then If you Want to deploy the model you should open the `Pycharm` and open the `streamlit_app.py` in the terminal run the following Command `streamlit run streamlit_app.py`
