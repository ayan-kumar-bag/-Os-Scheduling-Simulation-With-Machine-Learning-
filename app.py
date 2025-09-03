import streamlit as st
import pandas as pd
from process import Process
from scheduling import fcfs, sjf, round_robin
from ml_scheduler import predict_algorithm

st.title("OS Scheduling Algorithms with Machine Learning")

# File uploader
data = st.file_uploader("Upload Process CSV", type="csv")

if data:
    df = pd.read_csv(data)
else:
    df = pd.DataFrame(columns=["PID", "Arrival Time", "Burst Time", "Priority"])

st.subheader("Uploaded Processes")
st.dataframe(df)

# Algorithm selection
algo = st.selectbox("Choose Algorithm", ["FCFS", "SJF", "Round Robin", "ML (recommended)"])
quantum = st.number_input("Quantum (only for Round Robin)", min_value=1, value=2)

# Run scheduling
if st.button("Run"):
    proc_list = [
        Process(row["PID"], row["Arrival Time"], row["Burst Time"], row["Priority"])
        for _, row in df.iterrows() if not pd.isnull(row["PID"])
    ]

    if algo == "FCFS":
        result = fcfs(proc_list)
    elif algo == "SJF":
        result = sjf(proc_list)
    elif algo == "Round Robin":
        result = round_robin(proc_list, quantum)
    elif algo == "ML (recommended)":
        best = predict_algorithm(proc_list)
        st.write(f"ML suggests: {best}")
        if best == "FCFS":
            result = fcfs(proc_list)
        elif best == "SJF":
            result = sjf(proc_list)
        elif best == "Round Robin":
            result = round_robin(proc_list, quantum)
        else:
            result = []
    else:
        result = []

    st.subheader("Schedule (PID, Start, Finish)")
    st.dataframe(pd.DataFrame(result, columns=["PID", "Start", "Finish"]))

# Developer section
st.markdown("---")
st.markdown("### 👨‍💻 Developed by")

col1, col2 = st.columns(2)

with col1:
    st.image("soumyajit.jpg", caption="Soumyajit Khan", width=200)

with col2:
    st.image("ayan.jpg", caption="Ayan Kumar Bag", width=200)
