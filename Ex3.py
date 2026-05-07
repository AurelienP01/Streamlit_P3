import streamlit as st
import pandas as pd
from streamlit_authenticator import Authenticate
from streamlit_option_menu import option_menu

df = pd.read_csv("user.csv")

lesDonneesDesComptes = {
    'usernames': {
        row['name']: {
            'name': row['name'],
            'password': row['password'],
            'email': row['email'],
            'failed_login_attemps': 0,
            'logged_in': False,
            'role': row['role']
        }
        for _, row in df.iterrows()
    }
}

authenticator = Authenticate(
    lesDonneesDesComptes,
    "cookie name",
    "cookie key",
    30,
)

authenticator.login()

def accueil():
    username = st.session_state["username"]
    role = lesDonneesDesComptes["usernames"][username]["role"]

    with st.sidebar:
        selection = option_menu(
            menu_title=f"Bienvenue {st.session_state['name']}",
            options=["Accueil", "Photos"]
        )
        authenticator.logout("Déconnexion")  # ← ici dans la sidebar

    if selection == "Accueil":
        st.markdown("<h1 style='font-size:40px;'>Bienvenue sur la page d'accueil !</h1>", unsafe_allow_html=True)
        st.image("Image_1.jpeg")

    elif selection == "Photos":
        st.markdown("<h1 style='font-size:40px;'>Mon trek 2025 - Grand-Bornand ! </h1>", unsafe_allow_html=True)
        
        col1, col2, col3 = st.columns(3)

        with col1:
            st.image("1.jpg")

        with col2:
            st.image("2.jpg")

        with col3:
            st.image("3.jpg")

if st.session_state["authentication_status"]:
    accueil()

elif st.session_state["authentication_status"] is False:
    st.error("L'username ou le password est/sont incorrect")

elif st.session_state["authentication_status"] is None:
    st.warning('Les champs username et mot de passe doivent être remplis')