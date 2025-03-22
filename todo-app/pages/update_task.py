

import streamlit as st

all_tasks = []

with open(r'database\task.txt','r') as f:
    tasks = f.readlines()
    all_tasks = [task.strip() for task in tasks]
for i in all_tasks:
    st.write(i)
update_task = st.text_input("Select item to be updated..")
new_task = st.text_input("Enter new task..")
if st.button('Update'):
    if update_task in all_tasks:
        index = all_tasks.index(update_task)
        all_tasks[index] = new_task
        with open(r'database\task.txt','w') as f:
            for task in all_tasks:
                f.write(task + '\n')
        st.success(f'{update_task} updated to {new_task}')
    else:
        st.error(f'{update_task} not found')
    st.subheader('Updated Task')
    
    st.write(new_task)
    
            