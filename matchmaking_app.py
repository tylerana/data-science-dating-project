# import ast
import streamlit as st
import pandas as pd

from app_utils.utils_location import create_location_lookup, get_profiles_within_radius
from app_utils.utils_matches import get_matches
from app_utils.utils_essay import process_user_essay
from app_utils.utils_embed import embed_user_essay
from app_utils.utils_essay_similarity import score_profiles

df = pd.read_csv("data/processed/profiles_sampled_for_app.csv")

def render_preferences_form(mode):
    form_key = f"user_preferences_{mode}"
    form_scope = st.sidebar if mode == "sidebar" else st

    with st.container():
        with form_scope.form(form_key):
            # preferred age of partner
            preferred_age = st.slider("🔮 Ideal age range", 18, 99, (25, 35))
            st.markdown("<hr style='border: none; margin: 0.1em 0;'>", unsafe_allow_html=True)

                
            # user gender
            user_gender = st.multiselect("✨ What’s your gender?", options=["Woman", "Man"])
            st.markdown("<hr style='border: none; margin: 0.1em 0;'>", unsafe_allow_html=True)
                
            # preferred matches
            preferred_matches = st.multiselect("💗 I'd like to be matched with ...", options=["Women", "Men"])
            st.markdown("<hr style='border: none; margin: 0.1em 0;'>", unsafe_allow_html=True)
            st.markdown(
                "<small style='color:gray;'>This project currently supports binary gender matching only due to dataset limitations.</small>",
                unsafe_allow_html=True)

                
            user_location = st.selectbox("📍 Location", options=all_locations, help="Start typing your city and state, like 'New York, NY'")
            user_location = user_location.lower() # have to convert it back for dictionary lookup
            user_radius = st.slider("👟 Match Radius (miles)", min_value=0, max_value=100, value=5)

            # question placeholder css 
            st.markdown("""
            <style>
            textarea::placeholder {
                color: gray !important;
                opacity: 1; 
            }
            </style>
            """, unsafe_allow_html=True)
            
            q1 = st.text_area("1. How would your closest friends describe you? (max 500 characters):", placeholder = "Probably ...", max_chars=500, key=f'q1_{mode}')
            q2 = st.text_area("2. What are you passionate about or spend time doing? (max 500 characters):", placeholder = "I am passionate about ...", max_chars=500, key=f'q2_{mode}')
            q3 = st.text_area("3. What are you looking for in a partner or relationship? (max 500 characters):", placeholder = "I am looking for someone who ... ", max_chars=500, key=f'q3_{mode}')
            q4 = st.text_area("4. Anything else you'd like to share that reflects who you are? (max 500 characters):", placeholder = "In a zombie apocalypse I would bring ...", max_chars=500, key=f'q4_{mode}')
            
            
            
            with st.expander("Advanced Options"):

                essay_weight = st.slider("Essay Score Weight", 0.0, 1.0, 0.7)
                num_matches = st.selectbox("Number of Matches to Show", options=[5, 10, 25])
                
            submit = st.form_submit_button("Find Matches 💗")
            
            return {
                "preferred_age": preferred_age,
                "user_gender": user_gender,
                "preferred_matches": preferred_matches,
                "user_location": user_location,
                "user_radius": user_radius,
                "q1": q1,
                "q2": q2,
                "q3": q3,
                "q4": q4,
                "essay_weight": essay_weight,
                "num_matches": num_matches,
                "submit": submit
            }
    
# location logic
location_lookup = create_location_lookup(df)
all_locations = sorted([loc.title() for loc in location_lookup.keys()])


st.markdown("""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Pinyon+Script&display=swap');
        
        /* html, body, [data-testid="stAppViewContainer"], [data-testid="stAppViewContainer"] > .main {
            background-color: #A0001C !important;
            color: white;
        } */
        
        .block-container {
            padding-top: 2rem;
            padding-left: 2rem;
            padding-right: 2rem;
        }
        
        /* sidebar
        [data-testid="stSidebar"] {
            background-color: #7a0014 !important;
        } */
        
        .motif-title {
            font-family: 'Pinyon Script', cursive;
            font-size: 4em;
            color: #A0001C;
            text-align: center;
            margin-top: 1em;
        }
        .motif-subtitle {
            font-size: 1.2em;
            color: #A0001C;
            text-align: center;
            font-family: Lora, serif;
            margin-bottom: 1em;
        }
        .motif-description {
            font-family: Lora, serif;
            font-size: 1.2em;
            text-align: center;
            color: #A0001C;
            margin-bottom: 0.5em;
        }
        
        .match-desc {
            font-family:'Pinyon Script', cursive;
            font-size: 2.0em;
            text-align: left;
            color: #A0001C;
            letter-spacing:0.02em;
            margin-top:1em;
        }
        
        textarea::placeholder {
            color: gray !important;
            opacity: 1;
        }
    </style>
    """, unsafe_allow_html=True)

st.markdown("<div class='motif-title'>Motif</div>", unsafe_allow_html=True)
st.markdown("<div class='motif-subtitle'>A Data-Driven Matchmaking App</div>", unsafe_allow_html=True)
st.markdown("""
    <div class='motif-description'>
        <strong>Your words. Your lifestyle. No pictures.</strong><br>
        Just smart matchmaking based on what <em>actually</em> matters.
    </div>
""", unsafe_allow_html=True)
st.markdown("<hr style='border: none; margin: 0.02em 0;'>", unsafe_allow_html=True)   
if "submitted" not in st.session_state or not st.session_state["submitted"]:
    form_data = render_preferences_form(mode="main")

    if form_data["submit"]:
        if form_data["user_location"] in location_lookup:
                user_coords = location_lookup[form_data["user_location"]]
                filtered_df = get_profiles_within_radius(
                    user_lat=user_coords[0],
                    user_lon=user_coords[1],
                    radius=form_data["user_radius"],
                    df=df
                )
                st.session_state["filtered_profiles"] = filtered_df
        else:
            st.warning("Location not found in dataset.")
            st.stop()
            
        st.session_state["preferences"] = {
            "sex": form_data["preferred_matches"],
            "age": form_data["preferred_age"], 
            "location": form_data["user_location"],
            "radius": form_data["user_radius"],
            "combined_user_essay": form_data["q1"] + form_data["q2"] + form_data["q3"] + form_data["q4"],
            "num_of_matches": form_data["num_matches"]
        }

        gender_mapping = { "Women": "f", "Men":"m"}
        mapped_matches = [gender_mapping[choice] for choice in form_data["preferred_matches"]]
        
        if not mapped_matches:
            st.warning("Please select at least one gender to match with.")
            st.stop()    
        
        df = st.session_state["filtered_profiles"]
        df = df[df["sex"].isin(mapped_matches)]
        final_df = df[(df["age"] >= form_data["preferred_age"][0]) & (df["age"] <= form_data["preferred_age"][1])]

        if final_df.empty:
            st.warning("0 profiles found. Please consider widening the age range or match radius.")
            st.stop()
            
        cleaned_essay = process_user_essay(st.session_state["preferences"]["combined_user_essay"])
        user_embedding = embed_user_essay(cleaned_essay)
                  
        top_profiles = score_profiles(user_embedding, final_df, form_data["num_matches"])
        top_profiles = pd.DataFrame(top_profiles)
        st.session_state["top_profiles"] = top_profiles
        st.session_state["match_index"] = 0
        st.session_state["submitted"] = True
        
        

elif st.session_state["submitted"]:
        form_data = render_preferences_form(mode="sidebar")
        
        if "top_profiles" in st.session_state and len(st.session_state["top_profiles"]) > 0:
            top_profiles = st.session_state["top_profiles"]
            st.markdown("<div class='match-desc'>Your Top Matches: </div>", unsafe_allow_html=True)
            
            for idx, row in top_profiles.iterrows():
                age = row["age"]
                location = row["location"].title()
                match_percent = round(row["similarity_score"] * 100, 2)
                match_snippet = row.get("You should message me if ...", "")
            
                if pd.isna(match_snippet) or match_snippet.strip() == "":
                    match_snippet = "They didn't say - maybe that's part of the mystery ✨"
                elif len(match_snippet) > 250:
                    match_snippet = match_snippet[:247] + "..."

            
                st.markdown(f"""
                <div style="border: 1px solid #e1e4e8; border-radius: 10px; padding: 10px; margin-bottom:20px; background: #A0001C; box-shadow: 2px 2px 10px rgba(0,0,0,0.05);">
                        <div style="font-size: 18px; font-weight: bold; color: #FFF; margin-bottom: 10px;">
                        💘 Someone near you
                        </div>
                        <div style="color: #FFF; font-size: 18px; margin-bottom: 10px;">
                        <strong>Age:</strong> {age} &nbsp; | &nbsp; <strong>Location:</strong> {location} &nbsp; | &nbsp; <strong>Match Percent:</strong> {match_percent} %
                        </div>
                        <div style="font-style: italic; color: #FFF; font-size: 18px;">
                        <strong> You should message me if ... </strong>
                        <br>
                        {match_snippet}
                        </div>
                </div>
                """, unsafe_allow_html=True)
        else:
            st.warning("No matches to display. Please try adjusting your preferences.")
