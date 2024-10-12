import streamlit as st


def authenticated_menu():
    # st.sidebar.image("/workspaces/blank-app/лого.png", use_column_width=True)
    st.sidebar.image("лого.png", use_column_width=True)

    hide_img_fs = '''
    <style>
    button[title="View fullscreen"]{
        visibility: hidden;}
    </style>
    '''

    st.sidebar.markdown(hide_img_fs, unsafe_allow_html=True)
    st.sidebar.page_link("streamlit_app.py", label="Chat")
    st.sidebar.page_link("pages/doc.py", label="Database")
    # if st.session_state.role in ["admin", "super-admin"]:
    #     st.sidebar.page_link("pages/admin.py", label="Manage users")
    #     st.sidebar.page_link(
    #         "pages/super-admin.py",
    #         label="Manage admin access",
    #         disabled=st.session_state.role != "super-admin",
    #     )


# def unauthenticated_menu():
#     st.sidebar.image("/workspaces/blank-app/лого.png", use_column_width=True)
#     # Show a navigation menu for unauthenticated users
#     st.sidebar.page_link("streamlit_app.py", label="Log in")


def menu():
    # Determine if a user is logged in or not, then show the correct
    # navigation menu
    # if "role" not in st.session_state or st.session_state.role is None:
    #     unauthenticated_menu()
    #     return
    authenticated_menu()


def menu_with_redirect():
    # Redirect users to the main page if not logged in, otherwise continue to
    # render the navigation menu
    # if "role" not in st.session_state or st.session_state.role is None:
    # st.switch_page("streamlit_app.py")
    menu()