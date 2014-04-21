##Task Sheet 1 Questions

# Task 3(a)

1. The function you need to get the player's name is GetPlayerName().
2. Check the length of the name, if the length of the name they entered was 0, ask for them to enter it again.
3. Variable that needs to be added will be called 'leaderboard' and will be boolean.

## Pseudo-Code

	FUNCTION GetPlayerName()
		PlayerName = INPUT ''Please enter your name: ''
		WHILE LEN(PlayerName) == 0:
			OUPUT ''You must enter something for your name.''
			PlayerName = INPUT ''Please enter your name: ''
		RETURN PlayerName
			END WHILE
	END FUNCTION

# Task 3(b)

1. The function that adds the scores to the table is UpdateRecentScores()

# Task 5

1. You need to import the datetime module to add the date to the scores.
2. DisplayRecentScores, UpdateRecentScores, ResetRecentScores
3. Using the conversion of datetime.date.strftime