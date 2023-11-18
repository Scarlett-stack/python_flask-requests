

def calculate_bonus(nr_games, asked_goals, scored_goals):
    prima = 0
    i = 0
    while i < nr_games:
        diff = asked_goals[i] - scored_goals[i]
        print("diff: ",diff)
        if diff <= 0:
            prima += 1000
            nr = (-1) * diff
            prima += nr * 800
        if diff > 0:
            prima -= diff * 200
            if prima < 0:
                prima = 0
        print("prima: ", prima)
        i += 1
    return prima


def print_bonus(nr_games, asked_goals, scored_goals):
    print("Total prime: ", calculate_bonus(nr_games, asked_goals, scored_goals))

if __name__ == '__main__':
    asked_goals = []
    scored_goals = []
    nr_games = int(input())
    for game in range(nr_games):
        asked, scored = map(int, input().split())
        asked_goals.append(asked)
        scored_goals.append(scored)
    print_bonus(nr_games, asked_goals, scored_goals)