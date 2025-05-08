import streamlit as st
import pandas as pd
import numpy


with st.sidebar:
    st.markdown("""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Pinyon+Script&display=swap');

        .sidebar-title {
            font-family: 'Pinyon Script', cursive;
            font-size: 2.8em;
            color: #7C1E28;
            text-align: center;
            margin-top: -1.5em;
        }
                
        .sidebar-subtitle {
            
            font-size: 1.0em;
            color: #7C1E28;
            text-align: center;
            font-family: Lora, serif;
            margin-bottom: .6em;
        }
        </style>

        <div class="sidebar-title">Motif</div>
        <div class="sidebar-subtitle"> A Data-Driven Matchmaking App</div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div style='font-family: Lora, serif; font-size: 1.0em; text-align: center; color: #7C1E28;'>
        <strong>Your words. Your lifestyle. No pictures.</strong><br>
        Just smart matchmaking based on what <em>actually</em> matters.
    </div>
    """, unsafe_allow_html=True)

     
    _ = """st.header("Select Your Preferences")"""

    st.markdown("<hr style='border: none; margin: 0.02em 0;'>", unsafe_allow_html=True)

    # preferred age of partner
    preferred_age = st.slider("🔮 Ideal age range", 18, 99, (25, 35))
    st.markdown("<hr style='border: none; margin: 0.1em 0;'>", unsafe_allow_html=True)

    
    # user gender
    st.multiselect("✨ What’s your gender?", options=["Woman", "Man"])
    st.markdown("<hr style='border: none; margin: 0.1em 0;'>", unsafe_allow_html=True)
    
    # preferred matches
    preferred_matches = st.multiselect("💗 I'd like to be matched with ...", options=["Women", "Men"])
    st.markdown("<hr style='border: none; margin: 0.1em 0;'>", unsafe_allow_html=True)

    user_location = st.multiselect("📍 Location", options=all_locations)

    st.markdown(
        "<small style='color:gray;'>This project currently supports binary gender matching only due to dataset limitations.</small>",
        unsafe_allow_html=True)
    
    with st.expander("Advanced Options"):
        essay_weight = st.slider("Essay Score Weight", 0.0, 1.0, 0.7)
        lifestyle_weight = st.slider("Lifestyle Score Weight", 0.0, 1.0, 0.7)
        num_matches = st.selectbox("Number of Matches to Show", options=[5, 10, 25])


