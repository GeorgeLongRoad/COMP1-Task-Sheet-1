##Task Sheet 1 Questions

# Task 3(a)

1. The function you need to get the player's name is GetPlayerName().
2. Check the length of the name, if the length of the name they entered was 0, ask for them to enter it again.
3. Variable that needs to be added will be called 'leaderboard' and will be boolean.

## Pseudo-Code

	FUNCTION GetPlayerName()
		Leaderboard = INPUT ''DO you want to add your score to the high score table? (y or n):
		IF Leaderboard[0].lower() <- 'y' THEN
			OUTPUT '' ''
			PlayerName = INPUT ''Please enter your name: ''
			WHILE LEN(PlayerName) == 0:
				OUPUT ''You must enter something for your name.''
				PlayerName = INPUT ''Please enter your name: ''
			END WHILE
		ELSE IF Leaderboard[0].lower() <- 'n' THEN
			CALL DisplayMenu
			CALL GetMenuChoice
