import pandas as pd


def preprocess_data():

    deliveries = pd.read_csv('../data/raw/deliveries.csv')
    matches = pd.read_csv('../data/raw/matches.csv')

    # Total runs in first innings
    total_run = deliveries.groupby(
        ['match_id', 'inning']
    )['total_runs'].sum().reset_index()

    total_run = total_run[total_run['inning'] == 1]
    total_run['total_runs'] = total_run['total_runs'] + 1

    match = pd.merge(
        matches,
        total_run[['match_id', 'total_runs']],
        left_on='id',
        right_on='match_id'
    )

    teams = [
        'Sunrisers Hyderabad',
        'Mumbai Indians',
        'Royal Challengers Bangalore',
        'Kolkata Knight Riders',
        'Kings XI Punjab',
        'Chennai Super Kings',
        'Rajasthan Royals',
        'Delhi Capitals'
    ]

    match['team1'] = match['team1'].replace(
        'Deccan Chargers',
        'Sunrisers Hyderabad'
    )

    match['team2'] = match['team2'].replace(
        'Deccan Chargers',
        'Sunrisers Hyderabad'
    )

    match['team1'] = match['team1'].replace(
        'Delhi Daredevils',
        'Delhi Capitals'
    )

    match['team2'] = match['team2'].replace(
        'Delhi Daredevils',
        'Delhi Capitals'
    )

    match = match[match['team1'].isin(teams)]
    match = match[match['team2'].isin(teams)]

    match = match[match['dl_applied'] == 0]

    match = match[['match_id', 'city', 'total_runs', 'winner']]

    delivery = pd.merge(
        match,
        deliveries,
        on='match_id'
    )

    delivery = delivery[delivery['inning'] == 2]


    # Feature engineering
    delivery['curr_score'] = delivery.groupby(
        ['match_id']
    )['total_runs_y'].cumsum()

    delivery['runs_required'] = (
        delivery['total_runs_x']
        - delivery['curr_score']
    )

    delivery['balls_left'] = (
        126 - (delivery['over'] * 6 + delivery['ball'])
    )

    delivery['player_dismissed'] = (
        delivery['player_dismissed']
        .fillna("0")
        .apply(lambda x: 0 if x == "0" else 1)
    )

    wickets = delivery.groupby(
        'match_id'
    )['player_dismissed'].cumsum().values

    delivery['wickets_left'] = 10 - wickets

    delivery['curr_run_rate'] = (
        delivery['curr_score'] * 6
    ) / (120 - delivery['balls_left'])

    delivery['req_run_rate'] = (
        delivery['runs_required'] * 6
    ) / delivery['balls_left']

    delivery['result'] = delivery.apply(
        lambda row:
        1 if row['batting_team'] == row['winner']
        else 0,
        axis=1
    )

    final_df = delivery[
        [
            'batting_team',
            'bowling_team',
            'city',
            'runs_required',
            'balls_left',
            'wickets_left',
            'total_runs_x',
            'curr_run_rate',
            'req_run_rate',
            'result'
        ]
    ]

    final_df = final_df.dropna()

    final_df = final_df.query(
        'balls_left > 0 and wickets_left > 0 and runs_required > 0'
    )

    final_df.to_csv('../data/processed/final_df.csv', index=False)
