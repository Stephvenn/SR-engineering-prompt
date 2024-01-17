
def initializeArray(data):

    teams = list(data.keys())
    numTeams = len(teams)

    table = [[ "-" for i in range(numTeams + 1)] for j in range(numTeams + 2)]
    table[0][0] = "Tm"
    table[numTeams + 1][0] = "Tm"

    for i, team1 in enumerate(teams):
        table[0][i + 1] = team1
        table[i + 1][0] = team1
        table[numTeams + 1][i + 1] = team1
        for j, team2 in enumerate(teams):
            if i != j:
                table[i + 1][j + 1] = data[team1][team2]["W"]
            
    return table

def printTable(arr):
    for i in arr:
        for j in i:
            print(j, end="\t")
        print("")




def main(): 
    data = {
    'BRO': {
    'BSN': { 'W': 10, 'L': 12 },
    'CHC': { 'W': 15, 'L': 7 },
    'CIN': { 'W': 15, 'L': 7 },
    'NYG': { 'W': 14, 'L': 8 },
    'PHI': { 'W': 14, 'L': 8 },
    'PIT': { 'W': 15, 'L': 7 },
    'STL': { 'W': 11, 'L': 11 }
    },
    'BSN': {
    'BRO': { 'W': 12, 'L': 10 },
    'CHC': { 'W': 13, 'L': 9 },
    'CIN': { 'W': 13, 'L': 9 },
    'NYG': { 'W': 13, 'L': 9 },
    'PHI': { 'W': 14, 'L': 8 },
    'PIT': { 'W': 12, 'L': 10 },
    'STL': { 'W': 9, 'L': 13 }
    },
    'CHC': {
    'BRO': { 'W': 7, 'L': 15 },
    'BSN': { 'W': 9, 'L': 13 },
    'CIN': { 'W': 12, 'L': 10 },
    'NYG': { 'W': 7, 'L': 15 },
    'PHI': { 'W': 16, 'L': 6 },
    'PIT': { 'W': 8, 'L': 14 },
    'STL': { 'W': 10, 'L': 12 }
    },
    'CIN': {
    'BRO': { 'W': 7, 'L': 15 },
    'BSN': { 'W': 9, 'L': 13 },
    'CHC': { 'W': 10, 'L': 12 },
    'NYG': { 'W': 13, 'L': 9 },
    'PHI': { 'W': 13, 'L': 9 },
    'PIT': { 'W': 13, 'L': 9 },
    'STL': { 'W': 8, 'L': 14 }
    },
    'NYG': {
    'BRO': { 'W': 8, 'L': 14 },
    'BSN': { 'W': 9, 'L': 13 },
    'CHC': { 'W': 15, 'L': 7 },
    'CIN': { 'W': 9, 'L': 13 },
    'PHI': { 'W': 12, 'L': 10 },
    'PIT': { 'W': 15, 'L': 7 },
    'STL': { 'W': 13, 'L': 9 }
    },
    'PHI': {
    'BRO': { 'W': 8, 'L': 14 },
    'BSN': { 'W': 8, 'L': 14 },
    'CHC': { 'W': 6, 'L': 16 },
    'CIN': { 'W': 9, 'L': 13 },
    'NYG': { 'W': 10, 'L': 12 },
    'PIT': { 'W': 13, 'L': 9 },
    'STL': { 'W': 8, 'L': 14 }
    },
    'PIT': {
    'BRO': { 'W': 7, 'L': 15 },
    'BSN': { 'W': 10, 'L': 12 },
    'CHC': { 'W': 14, 'L': 8 },
    'CIN': { 'W': 9, 'L': 13 },
    'NYG': { 'W': 7, 'L': 15 },
    'PHI': { 'W': 9, 'L': 13 },
    'STL': { 'W': 6, 'L': 16 }
    },
    'STL': {
    'BRO': { 'W': 11, 'L': 11 },
    'BSN': { 'W': 13, 'L': 9 },
    'CHC': { 'W': 12, 'L': 10 },
    'CIN': { 'W': 14, 'L': 8 },
    'NYG': { 'W': 9, 'L': 13 },
    'PHI': { 'W': 14, 'L': 8 },
    'PIT': { 'W': 16, 'L': 6 }
    }}

    table = initializeArray(data)
    printTable(table)

main()