from operator import index
import streamlit as st  
import pandas as pd


def compute_elo(player1_elo, player2_elo):
    return 1/(1+10**((player2_elo - player1_elo)/400))
st.title("Elo Match Predictor")
st.info("An elo-rating based predictor to predict the outcomes of tennis matches. All elo ratings are derived from [1] http://tennisabstract.com/")

# loading the data
elo_ratings = pd.read_csv('tennis-players.csv')
elo_ratings['Player'] = elo_ratings['Player'].apply(lambda x:x.replace(u'\xa0',' '))

# 
PLAYERS = elo_ratings['Player'].tolist()
PLAYER_ELO = {}

# intializing the player dictionary
for p in PLAYERS:
    PLAYER_ELO[p] = elo_ratings[elo_ratings['Player'] == p]['Elo'].values[0]



player_1 = st.selectbox(
     'Player 1',
     PLAYERS)

player_2 = st.selectbox(
     'Player 2',
     PLAYERS,index=PLAYERS[4])
# st.write('You selected:', player_1,' vs ', player_2)
probability_elo = compute_elo(PLAYER_ELO[player_1], PLAYER_ELO[player_2])
# st.text(PLAYER_ELO[player_1])
# st.text(PLAYER_ELO[player_2])
if st.button("Compute"):
    st.code(f"Winning Chances")
    col1, col2= st.columns(2)
    col1.metric(" Player 1 ", f"{round(probability_elo*100,3)} %",delta="")
    col2.metric(" Player 2 ", f"{round((1-probability_elo)*100,3)} %",delta="")
