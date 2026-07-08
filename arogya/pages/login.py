import streamlit as st


def show():

    left, right = st.columns([1, 1])

    with left:

        st.markdown("# 🌿 ArogyaAI")
        st.markdown("### Guiding Care with Intelligence")

        st.write("")

        username = st.text_input(
            "Username",
            placeholder="Enter Username"
        )

        password = st.text_input(
            "Password",
            placeholder="Enter Password",
            type="password"
        )

        col1, col2 = st.columns([1,1])

        with col1:
            st.checkbox("Remember Me")

        with col2:
            st.markdown(
                "<p style='text-align:right;color:#4CAF50;'>Forgot Password?</p>",
                unsafe_allow_html=True
            )

        st.button(
            "Login",
            use_container_width=True
        )

        st.markdown(
            "<center>New User? <span style='color:#4CAF50;'>Register</span></center>",
            unsafe_allow_html=True
        )

    with right:
        st.image(
            "arogya/assets/images/login_bg.png",
            use_container_width=True
        )