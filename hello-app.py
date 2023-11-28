import streamlit as st 

st.write('Hello World!')
import streamlit as st 
import pandas as pd
import time

st.markdown("# Hamming Code")
#st.markdown("This is Hamming Code for 15 bit.")
#----------------------------------------------#
def Hamming_Code7bit(input):
    input = str(input)

    #condition_pass = True
    #for i in input:
    #    if i != '0' and i != '1':
    #        st.error('Your Code Must be Binary.', icon="🚨")
    #        condition_pass = False
    #        break

    #if len(input) < 7 or len(input) > 7:
     #   st.error('Your Code Must be 7 digit.', icon="🚨")
     #   condition_pass = False

    #if condition_pass:   
    code = [int(x) for x in str(input)]
    df = pd.DataFrame(columns = ['Circle No.', 'Sum', '1','2','3','4','5','6','7'] ,index=[0,1,2])

    for i in range(3):
        df['Circle No.'][i] = i+1

    df = df.set_index('Circle No.')

    df['1'][1] = code[0]

    df['2'][2] = code[1]

    df['3'][1] = code[2]
    df['3'][2] = code[2]

    df['4'][3] = code[3]

    df['5'][1] = code[4]
    df['5'][3] = code[4]

    df['6'][2] = code[5]
    df['6'][3] = code[5]

    df['7'][1] = code[6]
    df['7'][2] = code[6]
    df['7'][3] = code[6]

    df = df.fillna(0)

    df['Sum'][1] = (df.iloc[0].sum())%2
    df['Sum'][2] = (df.iloc[1].sum())%2
    df['Sum'][3] = (df.iloc[2].sum())%2

    wrong_index = (2**0*df['Sum'][1])+(2**1*df['Sum'][2])+(2**2*df['Sum'][3])

    if wrong_index == 0:
            st.success('Your Code is correct!', icon="✅")
            return None
    else:
        if code[wrong_index-1] == 0:
            code[wrong_index-1] = 1
        elif code[wrong_index-1] == 1:
            code[wrong_index-1] = 0
                    
            #print(df)
            #print("wrong_index =", wrong_index)
            st.error(f"Your Code is incorrect at position: {wrong_index}")
            #print("Your Message is incorrect at position", wrong_index)

            correct_code = ''.join([str(x) for x in code])
            st.success(f'Your Code shoud be: {correct_code}', icon="✅")
            #print("Your Message shoud be:", correct_code)

#----------------------------------------------#
# Hamming Code
def Hamming_Code15bit(input):
    input = str(input)

    #condition_pass = True
    #for i in input:
    #    if i != '0' and i != '1':
    #        st.error('Your Code Must be Binary.', icon="🚨")
    #        condition_pass = False
    #       break

    #if len(input) < 15 or len(input) > 15:
    #    st.error('Your Code Must be 15 digit.', icon="🚨")
    #    condition_pass = False

    #if condition_pass:
    code = [int(x) for x in str(input)]
    df = pd.DataFrame(columns = ['Circle No.', 'Sum', '1','2','3','4','5','6','7','8','9','10','11','12','13','14','15'] ,index=[0,1,2,3])

    for i in range(4):
        df['Circle No.'][i] = i+1

    df = df.set_index('Circle No.')

    df['1'][1] = code[0]

    df['2'][2] = code[1]

    df['3'][1] = code[2]
    df['3'][2] = code[2]

    df['4'][3] = code[3]

    df['5'][1] = code[4]
    df['5'][3] = code[4]

    df['6'][2] = code[5]
    df['6'][3] = code[5]

    df['7'][1] = code[6]
    df['7'][2] = code[6]
    df['7'][3] = code[6]

    df['8'][4] = code[7]

    df['9'][1] = code[8]
    df['9'][4] = code[8]

    df['10'][2] = code[9]
    df['10'][4] = code[9]

    df['11'][1] = code[10]
    df['11'][2] = code[10]
    df['11'][4] = code[10]

    df['12'][3] = code[11]
    df['12'][4] = code[11]

    df['13'][1] = code[12]
    df['13'][3] = code[12]
    df['13'][4] = code[12]

    df['14'][2] = code[13]
    df['14'][3] = code[13]
    df['14'][4] = code[13]

    df['15'] = code[14]

    df = df.fillna(0)

    df['Sum'][1] = (df.iloc[0].sum())%2
    df['Sum'][2] = (df.iloc[1].sum())%2
    df['Sum'][3] = (df.iloc[2].sum())%2
    df['Sum'][4] = (df.iloc[3].sum())%2

    wrong_index = (2**0*df['Sum'][1])+(2**1*df['Sum'][2])+(2**2*df['Sum'][3])+(2**3*df['Sum'][4])

    if wrong_index == 0:
        st.success('Your Code is correct!', icon="✅")
        #print("Your Message is correct!")
        return None
    else:
        if code[wrong_index-1] == 0:
            code[wrong_index-1] = 1
        elif code[wrong_index-1] == 1:
            code[wrong_index-1] = 0
            
    #print(df)
    #print("wrong_index =", wrong_index)
    st.error(f"Your Code is incorrect at position: {wrong_index}")
    
    
    correct_code = ''.join([str(x) for x in code])
    st.success(f'Your Code shoud be: {correct_code}', icon="✅")

#------------------------------------------------------#
#                  UX UI

def check_condition(input):
    input = str(input)
    #st.write(input)
    for i in input:
        #st.write(i) 
        if i != '0' and i != '1':
            with st.spinner('Wait for it...'):
                time.sleep(1) 
            st.error('Your Code Must be Binary.', icon="🚨")
            #st.write("pass11")    
            return False

    if choose_bit == "***7 bits***":
        if len(input) < 7 or len(input) > 7:
            with st.spinner('Wait for it...'):
                time.sleep(1) 
            st.error('Your Code Must be 7 digit.', icon="🚨")
            #st.write("pass12")
            return False 
    else:
        if len(input) < 15 or len(input) > 15:
            with st.spinner('Wait for it...'):
                time.sleep(1) 
            st.error('Your Code Must be 15 digit.', icon="🚨")
            #st.write("pass13")
            return False
    
    return True


choose_bit = st.radio("Selected the number of bits",["***7 bits***", "***15 bits***"])

if choose_bit == "***7 bits***":
    st.write('You selected 7 bits.')
else:
    st.write("You selected 15 bits.")
    
Message = str(st.text_input("***Enter your Code***")).strip()
check_btn = st.button("Check!", type="primary")
#check_btn = st.form_submit_button("Check!")
#if check_btn or Message:
if check_btn :
    if check_condition(Message):
        #st.write("pass2")
        if choose_bit == "***7 bits***":
            with st.spinner('Wait for it...'):
                time.sleep(1)    
                Hamming_Code7bit(Message)
           # st.write("pass3")

        elif choose_bit == "***15 bits***":
            with st.spinner('Wait for it...'):
                time.sleep(1)   
                Hamming_Code15bit(Message)
            #st.write("pass4")
