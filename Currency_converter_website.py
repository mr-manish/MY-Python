import streamlit as st
import requests

# Getting that flashy animation on top
st.markdown('<iframe src="https://embed.lottiefiles.com/animation/9918"></iframe>', unsafe_allow_html=True)

# we separate space into 3 columns
col1, col2, col3 = st.columns(3)

# using column we made a box and the options are as follows
with col1:
    curr1 = st.selectbox('Currency 1', ['Rupee', 'Dollar', 'Euro', 'Yen'])

# using column we create images based on the users choice of col1
with col2:
    if curr1 == 'Rupee':
        st.markdown('<iframe src="https://embed.lottiefiles.com/animation/89274"></iframe>', unsafe_allow_html=True)
    elif curr1 == 'Dollar':
        st.markdown('<iframe src="https://embed.lottiefiles.com/animation/89427"></iframe>', unsafe_allow_html=True)
    elif curr1 == 'Euro':
        st.markdown('<iframe src="https://embed.lottiefiles.com/animation/43343"></iframe>', unsafe_allow_html=True)
    else:
        st.markdown('<iframe src="https://embed.lottiefiles.com/animation/23881"></iframe>', unsafe_allow_html=True)

# Giving user the chance what he wants his currency to convert
with col3:
    curr2 = st.selectbox('Currency 2', ['Rupee', 'Dollar', 'Euro', 'Yen'])

# Making currency dictionary,for api to understand what are we talking about
currency = {
    'Dollar': 'USD',
    'Rupee': 'INR',
    'Euro': 'EUR',
    'Yen': 'JPY'
}

# Making the url that can grab our info from the api
url = f'https://free.currconv.com/api/v7/convert?q={currency[curr1]}_{currency[curr2]},{currency[curr2]}_{currency[curr1]}&compact=ultra&apiKey=6cf1130eeca4e3733dbb'

# requesting the information to api
re = requests.get(url)
re = re.json()

# re above return a dictionary with names of type1_type2
one_two = re[f'{currency[curr1]}_{currency[curr2]}']
two_one = re[f'{currency[curr2]}_{currency[curr1]}']

# again separating our column space into two.We can use col1 and col2  again, and it doesn't give error
col1, col2 = st.columns(2)

# Displaying current value of curr1 to curr2
with col1:
    st.write(f'1 {curr1} to {curr2}')
    st.success(one_two)

# Displaying the current value of curr2 to curr1
with col2:
    st.write(f'1 {curr2} to {curr1}')
    st.success(two_one)

col1, col2 = st.columns(2)
# Giving user a chance how much money he wants to convert
with col1:
    amount = st.number_input(curr1)
# Displaying user how much his amount would weigh in selected choice
with col2:
    st.write(f'Your {amount} {curr1} is ')
    converted = amount * one_two
    st.success(converted)

# Removing the unnecessary elements from website
st.markdown('<style>body{text-align:center} #MainMenu{visibility : hidden}footer{visibility : hidden;} </style>', unsafe_allow_html=True)

# Choose (streamlit run [Pythonfile.name]) in terminal to run website
