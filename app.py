import streamlit as st
from process_steps import PROCESS_STEPS
from components import sidebar, main_content

def main():
    st.set_page_config(layout="wide", page_title="Operations Process Tracker")
    
    st.title("OpsMan Demo")

    # Initialize session state for step statuses and notes if not already present
    if 'step_status' not in st.session_state:
        st.session_state.step_status = {step['id']: False for step in PROCESS_STEPS}
    if 'step_notes' not in st.session_state:
        st.session_state.step_notes = {step['id']: "" for step in PROCESS_STEPS}

    # Create two columns: main content and sidebar
    col1, col2 = st.columns([8, 1])

    with col1:
        main_content(PROCESS_STEPS)

    with col2:
        sidebar(PROCESS_STEPS)

if __name__ == "__main__":
    main()