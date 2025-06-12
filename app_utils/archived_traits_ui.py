# TRAIT SELECTION
import streamlit as st 

# diet
st.markdown("Which diets are you open to in a partner?")

diet_options = [
("🥩 Anything", "anything"),
("🥦 Vegetarian", "vegetarian"),
("🥑 Vegan", "vegan"),
("🕌 Halal", "halal"),
("✡️ Kosher", "kosher"),
("🐟 Other", "other"),
("🤷 Unknown", "unknown")
]

if "preferred_diet" not in st.session_state:
    st.session_state["preferred_diet"] = []
    
diet_cols = st.columns(4)

for i, (label, value) in enumerate(diet_options):
    col = diet_cols[i % 4]
    with col:
        is_clicked = value in st.session_state["preferred_diet"]
        button_label = f"✅ {label}" if is_clicked else label
        
        if st.button(button_label, key=f"diet_{value}"):
            if is_clicked:
                st.session_state["preferred_diet"].remove(value)
            else:
                st.session_state["preferred_diet"].append(value)
# --------------------------------------------------------------           
        
# smokes
st.markdown("Which smoking habits are you okay with in a partner?")
smoke_options = [
    ("🚬 Regularly", "regularly"),
    ("💨 Occasionally", "occasionally"),
    ("😮‍💨 Trying to quit", "trying to quit"), 
    ("🚭 No", "no"),
    ("❓ Unknown", "unknown")
]   

if "preferred_smokes" not in st.session_state:
    st.session_state["preferred_smokes"] = []
    
smokes_cols = st.columns(4)

for i, (label, value) in enumerate(smoke_options):
    col = smokes_cols[i % 4]
    with col:
        is_clicked = value in st.session_state["preferred_smokes"]
        button_label = f"✅ {label}" if is_clicked else label
        
        if st.button(button_label, key=f"smokes_{value}"):
            if is_clicked:
                st.session_state["preferred_smokes"].remove(value)
            else:
                st.session_state["preferred_smokes"].append(value)
# --------------------------------------------------------------            

# drinks
st.markdown("Which drinking habits are fine with you in a match?")

drinks_options = [
    ("🍸 Often", "often"),
    ("🥂 Socially", "socially"),
    ("👎 Rarely/Not At All", "rarely/not at all"), 
    ("😭 Unknown", "unknown")
]   

if "preferred_drinks" not in st.session_state:
    st.session_state["preferred_drinks"] = []
    
drinks_cols = st.columns(4)


for i, (label, value) in enumerate(drinks_options):
    col = drinks_cols[i % 4]
    with col:
        is_clicked = value in st.session_state["preferred_drinks"]
        button_label = f"✅ {label}" if is_clicked else label
        
        if st.button(button_label, key=f"drinks_{value}"):
            if is_clicked:
                st.session_state["preferred_drinks"].remove(value)
            else:
                st.session_state["preferred_drinks"].append(value)

# --------------------------------------------------------------

# drinks
st.markdown("Which drinking habits are fine with you in a match?")

drinks_options = [
    ("🍸 Often", "often"),
    ("🥂 Socially", "socially"),
    ("👎 Rarely/Not At All", "rarely/not at all"), 
    ("😭 Unknown", "unknown")
]   

if "preferred_drinks" not in st.session_state:
    st.session_state["preferred_drinks"] = []
    
drinks_cols = st.columns(4)


for i, (label, value) in enumerate(drinks_options):
    col = drinks_cols[i % 4]
    with col:
        is_clicked = value in st.session_state["preferred_drinks"]
        button_label = f"✅ {label}" if is_clicked else label
        
        if st.button(button_label, key=f"drinks_{value}"):
            if is_clicked:
                st.session_state["preferred_drinks"].remove(value)
            else:
                st.session_state["preferred_drinks"].append(value)

# --------------------------------------------------------------



lifestyle_weight = st.slider("Lifestyle Score Weight", 0.0, 1.0, 0.3)







