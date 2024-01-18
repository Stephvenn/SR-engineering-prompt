# SR-engineering-prompt

Hello, My name is Stephen Shin and this is my submission for the Sports Reference Engineering Intern prompt

```
    teams = list(data.keys())
    numTeams = len(teams)

    table = [[ "-" for i in range(numTeams + 1)] for j in range(numTeams + 2)]
    table[0][0] = "Tm"
    table[numTeams + 1][0] = "Tm"
```
These lines turn the JSON into a list of all the teams, and create a table with the required size of fills it with -'s. Then it sets the top left and bottom left corner to Tm
```
    for i, team1 in enumerate(teams):
        table[0][i + 1] = team1
        table[i + 1][0] = team1
        table[numTeams + 1][i + 1] = team1
        for j, team2 in enumerate(teams):
            if i != j:
                table[i + 1][j + 1] = data[team1][team2]["W"]
```
Then, the lines above first loop through the list of teams and sets the headers on the top row and left column. Then, a second loop goes through each team again and fills in the cells by finding the data for the wins that team1 has against team2 in the JSON, skipping if team1 is the same as team2.
