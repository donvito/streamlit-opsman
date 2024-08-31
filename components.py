import streamlit as st

def sidebar(steps):
    st.sidebar.header("Process Overview")
    for step in steps:
        with st.sidebar.expander(f"{step['id']} {step['name']}"):
            status = "✅" if st.session_state.step_status[step['id']] else "❌"
            st.write(f"Status: {status}")
            st.write(f"Notes: {st.session_state.step_notes[step['id']]}")

def main_content(steps):
    for step in steps:
        with st.expander(f"{step['id']} {step['name']}", expanded=True):
            col1, col2 = st.columns([1, 3])
            with col1:
                st.checkbox(
                    "Completed",
                    key=f"checkbox_{step['id']}",
                    value=st.session_state.step_status[step['id']],
                    on_change=update_status,
                    args=(step['id'],)
                )
            with col2:
                st.text_area(
                    "Notes",
                    key=f"notes_{step['id']}",
                    value=st.session_state.step_notes[step['id']],
                    on_change=update_notes,
                    args=(step['id'],)
                )
            if step['highlighted']:
                st.warning("This step requires input into a system or documentation to be sent to a counterparty.")

def update_status(step_id):
    st.session_state.step_status[step_id] = st.session_state[f"checkbox_{step_id}"]

def update_notes(step_id):
    st.session_state.step_notes[step_id] = st.session_state[f"notes_{step_id}"]