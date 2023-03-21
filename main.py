from transformers import pipeline
import streamlit as st

st.title('Web-приложение для создания аннотаций к тексту')
st.markdown('Приложение использует предварительно обученную модель "IlyaGusev/rut5_base_sum_gazeta", полученную '
            'с Hugging Face (https://huggingface.co/) и используемую для обобщения текста на русском языке.')

text = st.text_area('Исходный текст:')


def run_model(input_text):
    input_text = str(input_text)
    model = pipeline("summarization", "IlyaGusev/rut5_base_sum_gazeta")
    output = model(input_text)
    st.write('Аннтоация')
    st.success(output[0]['summary_text'])


if st.button('Отправить текст...'):
    run_model(text)
