import streamlit as st
import pickle

# ================Assenment_Title============#
styled_text = "<p style='font-size: 30 px; font-weight: bold;color:magenta;'>Telecom Customer Churn Prediction:</p>"
st.markdown(styled_text, unsafe_allow_html=True)

col1, col2, col3 = st.columns([1, 1, 1])
with col1:
    gender_options = {"": [0, 0], "Male": [0, 1], "Female": [1, 0]}
    gender = st.selectbox("Select gender", list(gender_options.keys()))
with col2:
    senior_citizen_options = {"": [0, 0], "No": 0, "Yes": 1}
    senior_citizen = st.selectbox("Select SeniorCitizen", list(senior_citizen_options.keys()))
with col3:
    Partner_options = {"": [0, 0], "No": [1, 0], "Yes": [0, 1]}
    Partner = st.selectbox("Select Partner", list(Partner_options.keys()))

col3, col4, col5 = st.columns([1, 1, 1])
with col3:
    dependents_options = {"": [0, 0], "No": [1, 0], "Yes": [0, 1]}
    dependents = st.selectbox("Select Dependents", list(dependents_options.keys()))
with col4:
    PhoneService_options = {"": [0, 0], "No": [1, 0], "Yes": [0, 1]}
    PhoneService = st.selectbox("Select the PhoneService", list(PhoneService_options.keys()))
with col5:
    multiple_lines_options = {"": [0, 0], "No": [1, 0, 0], "No Phone Service": [0, 1, 0], "yes": [0, 0, 1]}
    multiple_lines = st.selectbox("Select MultipleLines", list(multiple_lines_options.keys()))

col7, col8, col9 = st.columns([1, 1, 1])
with col7:
    InternetService_option = {"": [0, 0, 0], "DSL": [1, 0, 0], "Fiber Optic": [0, 1, 0], "No": [0, 0, 1]}
    InternetService = st.selectbox("Select the InternetService", list(InternetService_option.keys()))
with col8:
    online_security_options = {"": [0, 0, 0], "No": [1, 0, 0], "No Internet Service": [0, 1, 0], "Yes": [0, 0, 1]}
    online_security = st.selectbox("Select OnlineSecurity", list(online_security_options.keys()))
with col9:
    online_backup_options = {"": [0, 0, 0], "No": [1, 0, 0], "No Internet Service": [0, 1, 0], "Yes": [0, 0, 1]}
    online_backup = st.selectbox("Select OnlineBackup", list(online_backup_options.keys()))

col10, col11, col12 = st.columns([1, 1, 1])
with col10:
    device_protection_options = {"": [0, 0, 0], "No": [1, 0, 0], "No Internet Service": [0, 1, 0], "Yes": [0, 0, 1]}
    device_protection = st.selectbox("Select DeviceProtection", list(device_protection_options.keys()))
with col11:
    tech_support_options = {"": [0, 0, 0], "No": [1, 0, 0], "No Internet Service": [0, 1, 0], "Yes": [0, 0, 1]}
    tech_support = st.selectbox("Select TechSupport", list(tech_support_options.keys()))
with col12:
    streaming_tv_options = {"": [0, 0, 0], "No": [1, 0, 0], "No Internet Service": [0, 1, 0], "Yes": [0, 0, 1]}
    streaming_tv = st.selectbox("Select StreamingTV", list(streaming_tv_options.keys()))

col13, col14, col15 = st.columns([1, 1, 1])
with col13:
    streaming_movies_options = {"": [0, 0, 0], "No": [1, 0, 0], "No Internet Service": [0, 1, 0], "Yes": [0, 0, 1]}
    streaming_movies = st.selectbox("Select StreamingMovies", list(streaming_movies_options.keys()))
with col14:
    contract_options = {"": [0, 0, 0], "Month to Month": [1, 0, 0], "One Year": [0, 1, 0], "Two Year": [0, 0, 1]}
    contract = st.selectbox("Select Contract", list(contract_options.keys()))
with col15:
    PaperlessBilling_options = {"": [0, 0], "No": [1, 0], "Yes": [0, 1]}
    PaperlessBilling = st.selectbox("Select PaperlessBilling", list(PaperlessBilling_options.keys()))

col16, col17, col18, col19 = st.columns([1, 0.6, 0.5, 0.7])
with col16:
    payment_methods_options = {
        "": [0, 0, 0, 0],
        " BankTransfer(Automatic)": [1, 0, 0, 0],
        "Creditcard(Automatic)": [0, 1, 0, 0],
        "Electronic Check": [0, 0, 1, 0],
        "Mailed Check": [0, 0, 0, 1]
    }

    payment_methods = st.selectbox("Select PaymentMethod", list(payment_methods_options.keys()))
with col17:
    MonthlyCharges = st.text_input("Enter the MonthlyCharges")
with col18:
    TotalCharges = st.text_input("Enter the TotalCharges")
with col19:
    tenure_groups_options = {
        "": [0, 0, 0, 0, 0, 0, 0, 0],
        "1-12 Months": [1, 0, 0, 0, 0, 0, 0, 0],
        "13-24 Months": [0, 1, 0, 0, 0, 0, 0, 0],
        "25-36 Months": [0, 0, 1, 0, 0, 0, 0, 0],
        "37-48 Months": [0, 0, 0, 1, 0, 0, 0, 0],
        "49-60 Months": [0, 0, 0, 0, 1, 0, 0, 0],
        "61-72 Months": [0, 0, 0, 0, 0, 1, 0, 0],
        "73-84 Months": [0, 0, 0, 0, 0, 0, 1, 0],
        "85-96 Months": [0, 0, 0, 0, 0, 0, 0, 1]
    }

    tenure_groups = st.selectbox("Select Tenure_Group", list(tenure_groups_options.keys()))

submit = st.button("Submit")
if submit:
    encoded_option = []
    encoded_option.append(senior_citizen_options[senior_citizen])
    encoded_option.append(int(MonthlyCharges))
    encoded_option.append(int(TotalCharges))
    for i in Partner_options[Partner]:
        encoded_option.append(i)
    for i in dependents_options[dependents]:
        encoded_option.append(i)
    for i in PhoneService_options[PhoneService]:
        encoded_option.append(i)
    for i in multiple_lines_options[multiple_lines]:
        encoded_option.append(i)
    for i in InternetService_option[InternetService]:
        encoded_option.append(i)
    for i in online_security_options[online_security]:
        encoded_option.append(i)
    for i in online_backup_options[online_backup]:
        encoded_option.append(i)
    for i in device_protection_options[device_protection]:
        encoded_option.append(i)
    for i in tech_support_options[tech_support]:
        encoded_option.append(i)
    for i in streaming_tv_options[streaming_tv]:
        encoded_option.append(i)
    for i in streaming_movies_options[streaming_movies]:
        encoded_option.append(i)
    for i in contract_options[contract]:
        encoded_option.append(i)
    for i in PaperlessBilling_options[PaperlessBilling]:
        encoded_option.append(i)
    for i in payment_methods_options[payment_methods]:
        encoded_option.append(i)
    for i in tenure_groups_options[tenure_groups]:
        encoded_option.append(i)

    load_model = pickle.load(open(r"C:\Users\arjun\PycharmProjects\pythonProject\model1.sav", 'rb'))
    predictions = load_model.predict([encoded_option])

    if predictions == [1]:
        st.success("Customer most likely to churn")
    else:
        st.success("Customer don't want to churn")
