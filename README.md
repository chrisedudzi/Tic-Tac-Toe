How the code works
-For the board I am using dictionary with nested lists
-The keys of the dictionary represents the positions on the board,top,bottom and middle
-The values are nested lists that keeps tracks of the input whether 'X' or "O" and and also  scores
-The nested lists initially conatin an empty and string and zero
-X has a value of 4
-O has a value of 3
-The inputs are in the form "top-1" where top refers to the top row and "1" is the first cell in the row
-To put this move on the board I split the input into two "top" and "1" the top would serve as the key and by subtracting one "1" would 
serve as the index for the nested list for tha specific key
-Each player is aasgined with either "X" or "O" at beginning of the game and dependin on whose turn it is the dictionary index 0 for the nested list
corresponding to that key is updated with either "X" or "O" and the index 1 is updated with either "4"or "3" respectively
-The program computes the total score after each input and compares it to what the score would be if someone won or the game is a draw
-I figured out what these scores would be for different configurations of the game and assigned them to variables
-WIN_STATEX=12-When there are three contiguous "X"s in any if the valid positions(Vertcal,horizontal or diagonal)
-WIN_STATEO=9-When there are three contiguous "O"s
-Draw occurs when there are 5 Xs and 4 Os or 4 Xs and 5 Os 
-DRAW_STATES=[31,32]- I found out for all different configurations for a draw the total score of the board would sum up to either 31 or 32 
