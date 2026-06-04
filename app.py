import pickle as pkl
import streamlit as st
import pandas as pd


teams = ['Sunrisers Hyderabad',
         'Mumbai Indians',
         'Royal Challengers Bangalore',
         'Kolkata Knight Riders',
         'Kings XI Punjab',
         'Chennai Super Kings',
         'Rajasthan Royals',
         'Delhi Capitals']


cities = ['Hyderabad', 'Bangalore', 'Mumbai', 'Indore', 'Kolkata', 'Delhi',
          'Chandigarh', 'Jaipur', 'Chennai', 'Cape Town', 'Port Elizabeth',
          'Durban', 'Centurion', 'East London', 'Johannesburg', 'Kimberley',
          'Bloemfontein', 'Ahmedabad', 'Cuttack', 'Nagpur', 'Dharamsala',
          'Visakhapatnam', 'Pune', 'Raipur', 'Ranchi', 'Abu Dhabi',
          'Sharjah', 'Mohali', 'Bengaluru']


pipe = pkl.load(open('./models/pipe.pkl', 'rb'))

st.title('IPL win prediction app')

col1, col2 = st.columns(2)


with col1:
    battingteam = st.selectbox('Select the bating team', sorted(teams))

with col2:
    bowlingteam = st.selectbox('Select the bowling team', sorted(teams))


city = st.selectbox('Select the city', sorted(cities))

target = int(st.number_input('Target', step=1))


col1, col2, col3 = st.columns(3)

with col1:
    score = int(st.number_input('score', step=1))

with col1:
    overs = int(st.number_input('Over completed', step=1))

with col1:
    wickets = int(st.number_input('wicket fallen', step=1))


if score > target:
    st.write(battingteam, "won the match")

elif score == target-1 and overs == 20:
    st.write("Match Drawn")

elif wickets == 10 and score < target-1:
    st.write(bowlingteam, 'Won the match')

elif wickets == 10 and score == target-1:
    st.write('Match tied')

elif battingteam == bowlingteam:
    st.write('To proceed, please select different teams because no match can be played between the same teams')

else:

    if target >= 0 and target <= 300 and overs >= 0 and overs <= 20 and wickets <= 10 and wickets >= 0 and score >= 0:
        try:
            if st.button('Predict probability'):
                runs_left = target-score

                balls_left = 120-(overs*6)

                wickets = 10-wickets

                currentrunrate = score/overs

                requiredrunrate = (runs_left*6)/balls_left

                input_df = pd.DataFrame(
                    {'batting_team': [battingteam],
                     'bowling_team': [bowlingteam],
                     'city': [city],
                     'runs_required': [runs_left],
                     'balls_left': [balls_left],
                     'wickets_left': [wickets],
                     'total_runs_x': [target],
                     'curr_run_rate': [currentrunrate],
                     'req_run_rate': [requiredrunrate]})

                result = pipe.predict_proba(input_df)

                lossprob = result[0][0]
                winprob = result[0][1]
                
                st.subheader(battingteam+"- "+str(round(winprob*100))+"%")

                st.subheader(bowlingteam+"- "+str(round(lossprob*100))+"%")

        except ZeroDivisionError:
            st.error("Please fill all the details")

        else:
            st.error(
                'There is something wrong with the input, please fill the correct details')
