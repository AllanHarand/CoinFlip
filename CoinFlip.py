import streamlit as st
import random

st.write('CoinFlip Game')


col1, col2, col3 = st.columns([1,2,1])

col1.markdown('Welcome 1')
col2.markdown('Welcome 2')
col3.markdown('Welcome 3')


starting_capital = st.number_input("Define your starting capital", min_value=10, value=100, help="Enter your starting capital here!")

#Betting type (fixed amount or percentage)

betting = st.radio('Betting fixed amount or percentage from remaining capital', ['Fixed amount', 'Percentage'])


probability = st.number_input("Define win probability", min_value=0.01, value=0.5, help="Enter winning probability for each run")

prob = st.slider(
    'Win percentage',
    min_value=0,
    max_value=100,
    value=50,
    step=1,
    format='%d%%')



prob_a = prob/100
prob_b = 1 - prob_a
runs = 100
#starting_capital = 1000
bet = 100
bet_pct = 0.5
samples = 100

st.write(prob)
st.write(prob_a)
st.write(prob_b)




def betting_fixed_amount():
    capital = starting_capital
    results = []

    for i in range(runs):
        if (capital > 0) and (capital >= bet):

            b = random.choices(population=['a', 'b'], weights=[prob_a, prob_b])
            if b == ['a']:
                capital = capital + bet
                results.append(capital)
            else:
                capital = capital - bet
                results.append(capital)

            # print(results)
        else:
            # results.append(capital)
            break

    print('---------------------')
    print('Visete tulemused: ')
    print('---------------------')

    print(results)
    return results

def betting_percentage():
    results = 'Betting percentage arvutusi veel ei ole'
    print(results)
    return results

result = st.button('RUN')
st.write(result)

if result:
    if betting == 'Fixed amount':
        st.write(betting_fixed_amount())
    if betting == 'Percentage':
        st.write(betting_percentage())

# Parameters
