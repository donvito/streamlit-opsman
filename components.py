import streamlit as st
from process_steps import PROCESS_STEPS

def sidebar(steps):
    st.sidebar.header("Process Overview")
    for step in steps:
        if step['type'] == 'main':
            sub_steps_completed = all(st.session_state.step_status.get(sub_step['id'], False) for sub_step in step['sub_steps'])
            status = '✅ Completed' if sub_steps_completed else '❌ Pending'
        else:
            status = '✅ Completed' if st.session_state.step_status.get(step['id'], False) else '❌ Pending'
        
        with st.sidebar.expander(f"{step['id']} {step['name']} {' ' * 3} {status.split()[0]}"):
            st.write(f"Status: {status}")
            if step['type'] == 'main':
                st.write(f"Sub-steps completed: {sum(st.session_state.step_status.get(sub_step['id'], False) for sub_step in step['sub_steps'])}/{len(step['sub_steps'])}")
                for sub_step in step['sub_steps']:
                    sub_status = '✅' if st.session_state.step_status.get(sub_step['id'], False) else '❌'
                    st.write(f"{sub_status} {sub_step['id']} {sub_step['name']}")
            st.write(f"Notes: {st.session_state.step_notes.get(step['id'], '')}")

def main_content(steps):
    for step in steps:
        is_completed = all(st.session_state.step_status.get(sub_step['id'], False) for sub_step in step['sub_steps']) if step['type'] == 'main' else st.session_state.step_status.get(step['id'], False)
        expander_color = "green" if is_completed else "default"
        with st.expander(f"{step['id']} {step['name']}", expanded=True):
            if expander_color == "green":
                st.markdown(f'<p style="background-color: #90EE90; padding: 10px; border-radius: 5px;">{step["id"]} {step["name"]}</p>', unsafe_allow_html=True)
            if step['type'] == 'main':
                for sub_step in step['sub_steps']:
                    col1, col2 = st.columns([1, 3])
                    with col1:
                        st.checkbox(
                            f"{sub_step['id']} {sub_step['name']}",
                            key=f"checkbox_{sub_step['id']}",
                            value=st.session_state.step_status.get(sub_step['id'], False),
                            on_change=update_status,
                            args=(sub_step['id'], step['id'])
                        )
                    with col2:
                        st.text_area(
                            "Notes",
                            key=f"notes_{sub_step['id']}",
                            value=st.session_state.step_notes.get(sub_step['id'], ''),
                            on_change=update_notes,
                            args=(sub_step['id'],)
                        )
                    if sub_step['highlighted']:
                        st.warning("This step requires input into a system or documentation to be sent to a counterparty.")
            else:
                col1, col2 = st.columns([1, 3])
                with col1:
                    st.checkbox(
                        "Completed",
                        key=f"checkbox_{step['id']}",
                        value=st.session_state.step_status.get(step['id'], False),
                        on_change=update_status,
                        args=(step['id'], None)
                    )
                with col2:
                    st.text_area(
                        "Notes",
                        key=f"notes_{step['id']}",
                        value=st.session_state.step_notes.get(step['id'], ''),
                        on_change=update_notes,
                        args=(step['id'],)
                    )
                if step['highlighted']:
                    st.warning("This step requires input into a system or documentation to be sent to a counterparty.")

def update_status(step_id, main_step_id=None):
    st.session_state.step_status[step_id] = st.session_state[f"checkbox_{step_id}"]
    if main_step_id:
        main_step = next(step for step in PROCESS_STEPS if step['id'] == main_step_id)
        sub_steps_completed = all(st.session_state.step_status.get(sub_step['id'], False) for sub_step in main_step['sub_steps'])
        st.session_state.step_status[main_step_id] = sub_steps_completed

def update_notes(step_id):
    st.session_state.step_notes[step_id] = st.session_state[f"notes_{step_id}"]