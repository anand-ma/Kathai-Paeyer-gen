import streamlit as st
from langchain_openai import ChatOpenAI
import os

os.environ["OPENAI_API_KEY"] = st.secrets["OPENAI_API_KEY"]

# Title and description
st.title("Kadhai Paeyar Gen")
st.markdown("Genrate a short name for the தமிழ் story passed") 
st.markdown("The prompt is automatically prepended the following: கீழே கொடுக்கப்பட்டுள்ள கதைக்குப் பொருத்தமான தலைப்பைக் கொடு. கதை: <Kathai>")

# Text input for topic
topic = st.text_input("Please enter the Kathai")

st.code("""
            Try:
            2050ல், இனியா ஒரு aerospace engineer ஆகி நிலாவில் மனிதரை அனுப்ப கனவு காண்கிறாள். ஆனால், project நிதியின்றி முடங்குகிறது.
            அவளின் அண்ணன் ஆனந்த், AI மூலம் உதவி செய்து NASAயின் ஆதரவை பெறுகிறார்.
            இறுதியில், இனியாவின் spacecraft நிலாவை சென்றடைந்து, அவள் வெற்றி பெறுகிறார்.
            அவள் நெகிழ்ந்து, "இந்த வெற்றி உன்னுடையது, அண்ணா!" என்று கூற, ஆனந்த் மகிழ்ச்சி அடைகிறான்.
        """, language= None)

# Initialize the models
base_model = ChatOpenAI(model="gpt-4o-mini")
ft_model = ChatOpenAI(model="ft:gpt-4o-mini-2024-07-18:freelancer:ama-ft:AzIdNxDF")

def generate_story_name(prompt, base_model=base_model, ft_model=ft_model):
    response1 = base_model.invoke(prompt)
    response2 = ft_model.invoke(prompt)
    return response1.content, response2.content

if st.button("Story Name"):
    if topic:
        with st.spinner("Thinking for an Approriate Name..."):
            base_response, ft_response = generate_story_name(f"கீழே கொடுக்கப்பட்டுள்ள கதைக்குப் பொருத்தமான தலைப்பைக் கொடு. கதை: {topic}")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.subheader("Base Model (gpt-4o-mini) 🔗")
            st.markdown(f'<div class="output-text">{base_response}</div>', unsafe_allow_html=True)
        
        with col2:
            st.subheader("Kathai Gen Model (Fine-tuned Model)")
            st.markdown(f'<div class="output-text">{ft_response}</div>', unsafe_allow_html=True)
    else:
        st.warning("Please enter a Story in தமிழ் to generate a name")

