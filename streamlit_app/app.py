import streamlit as st
import spacy
import pandas as pd
import numpy as np

nlp = spacy.load("en_core_web_sm")


st.title('Part of Speech Identifier')

title = st.text_input('Enter Text', '')

name = []
Noun = []

text = nlp(title)
for i in text:
    name.append(str(i))
    Noun.append(spacy.explain(i.pos_))

  #st.write(i, i.pos_,"------", spacy.explain(i.pos_))
  #st.write(name)
  #st.write(Noun)



df = pd.DataFrame({"Word":name,"Part of speech":Noun})


st.table(df)
