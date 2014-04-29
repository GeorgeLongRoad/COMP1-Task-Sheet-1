##Task Sheet 2 Questions

##Task 6 

1.
2. DisplayMenu
3. 

## Pseudo-Code

	FUNCTION DisplayOptions()
		OUTPUT 'OPTION MENU'
		OUTPUT ''
		OUTPUT '1. Set Ace to be HIGH or LOW'
		OUPTPUT ''
		OUTPUT ''

	FUNCTION GetOptionChoice()
		OptionChoice = INPUT 'Select an option from the menu (or enter q to quit): '
		OptionChoice = OptionChoice[0]
		OUTPUT ''
		RETURN OptionChoice

	FUNCTION SetOptions(OptionChoice)
		IF OptionChoice == "1" THEN
		SetAceHighLow()
		ELSE IF OptionChoice == "2" THEN
			pass
		END IF
    
	FUNCTION SetAceHighLow()
	GLOBAL High
	aceHL = INPUT 'Do you want ace to be high or low?(h/l): ".LOWER()
	High = FALSE
	IF aceHL == "h" THEN
		High = TRUE
	ELSE IF aceHL == "l" THEN
		High = FALSE
	END IF
	