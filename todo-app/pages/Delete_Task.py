

import streamlit as st

all_tasks = []



with open(r'database\task.txt','r') as f:
                tasks = f.readlines()
                all_tasks = [task.strip() for task in tasks]
                for task in all_tasks:
                    st.text(task)
                delete_task = st.text_input("Select item to be deleted..")
    
if st.button('Delete'):
    if delete_task in all_tasks:
        all_tasks.remove(delete_task)
        with open(r'database\task.txt','w') as f:
            for task in all_tasks:
                f.write(task + '\n')
        st.success(f'{delete_task}  deleted successfully')
    else:
        st.error(f'{delete_task} not found')
    st.subheader('Updated Task')
    
    st.write(task)
            