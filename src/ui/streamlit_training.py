import sys

import numpy as np
import pandas as pd
import streamlit as st
from sklearn.feature_extraction.text import CountVectorizer

sys.path.append('.')
from src.models.models_save_and_load import save_models
from src.models.models_train import fit_models, compute_CV_score_for_each_class
from src.conf.global_variables import LABELS, COMMENT_COLUMN
from src.data.feature_engineering import preprocess_train_df, tokenize

st.title('Entraînement du modèle')

st.subheader("Fichier d'entraînement")
csv_file = st.file_uploader('Drop a csv file to train on:', type=['csv'])
if csv_file is not None:
    train_df = pd.read_csv(csv_file)
    st.dataframe(train_df.head())

    with st.spinner('Preprocessing data...'):
        train_df = preprocess_train_df(train_df, COMMENT_COLUMN)
        vectorizer = CountVectorizer(ngram_range=(1, 1), tokenizer=tokenize,
                                     min_df=3, max_df=0.9, strip_accents='unicode')
        trn_term_doc = vectorizer.fit_transform(train_df[COMMENT_COLUMN])
        X = trn_term_doc
        y = train_df[LABELS]
        st.success('Data processed.')

    with st.spinner('Computing cross validation scores for each class...'):
        cv_scores = compute_CV_score_for_each_class(X, y, LABELS)
        mean_cv_scores = np.mean(cv_scores)
        st.success(f'Mean cross-validated AUC score: {mean_cv_scores}')

    with st.spinner('Training models...'):
        all_classifiers = fit_models(X, y, LABELS)
        save_models(all_classifiers, vectorizer)
        st.success('Models trained and saved.')