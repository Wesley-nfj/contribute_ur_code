import streamlit as st

st.markdown(
    """
  <style>
    .stApp{
        background-color: #ff0015;
    }    

   </style>                    
     """,
unsafe_allow_html=True
)


st.title("TO-DO LIST app ")
task= st.text_input("Enter your task",)

if "tasks" not in st.session_state:
    st.session_state.tasks =[]
     
if st.button("Add task"):
    if task:
        st.session_state.tasks.append(task)
       
    else:
        st.warning("Please Add a task")
    
completed_task=[]
for i, task in enumerate(st.session_state.tasks):
    col1, col2 =st.columns([0.7, 0.3])
    with col1:
      st.checkbox(task, key= f"task{i}")
    with col2:
      if st.button('X', key=f"delet_{i}"):
         st.session_state.tasks.pop(i)
      
      
