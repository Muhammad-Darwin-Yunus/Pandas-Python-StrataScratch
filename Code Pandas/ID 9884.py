>.<

Title: Find the team division of each player
Link: https://platform.stratascratch.com/coding/9884-find-the-team-division-of-each-player?code_type=2
Level: Easy

Find the team division of each player.
Output the player name along with the corresponding team division.

Data college_football_teams:
conference: text
division: text
id: bigint
roster_url: text
school_name: text

Data college_football_players:
full_school_name: text
height: bigint
hometown: text
id: bigint
player_name: text
position: text
school_name: text
state: text
weight: bigint
year: text

>.<

Solution:

# Import your libraries
import pandas as pd

# Start writing code

college_football_teams = pd.merge(college_football_teams,college_football_players,left_on='id',right_on='id',how='inner')

college_football_teams[['player_name','division']]
    
Output:

player_name                |  division
Ralph Abernathy              FBS (Division I-A Teams)
Mekale McKay                  FBS (Division I-A Teams)
Trenier Orr                  FBS (Division I-A Teams)
Bennie Coney                  FBS (Division I-A Teams)
Johnny Holton                FBS (Division I-A Teams)
Howard Wilder                FBS (Division I-A Teams)
Munchie Legaux                FBS (Division I-A Teams)
Mark Barr                    FBS (Division I-A Teams)
Aaron Brown                  FBS (Division I-A Teams)
Anthony McClung              FBS (Division I-A Teams)
Tion Green                    FBS (Division I-A Teams)
Mike Tyson                    FBS (Division I-A Teams)
Gunner Kiel                  FBS (Division I-A Teams)
Adrian Witty                  FBS (Division I-A Teams)
Patrick Coyne                  FBS (Division I-A Teams)
Dionne Thrweatt-Vassar        FBS (Division I-A Teams)
Jordan Luallen                FBS (Division I-A Teams)
Deven Drane                    FBS (Division I-A Teams)
Brendon Kay                    FBS (Division I-A Teams)
Leviticus Payne                FBS (Division I-A Teams)
Grant Coleman                  FBS (Division I-A Teams)
Tony Miliano                    FBS (Division I-A Teams)
Chris Moore                    FBS (Division I-A Teams)
Michael Colosimo              FBS (Division I-A Teams)
Jeremy Graves                  FBS (Division I-A Teams)
Tyler Cogswell                FBS (Division I-A Teams)
Derek Cox                      FBS (Division I-A Teams)
Shaq Washington                FBS (Division I-A Teams)
Tshumbi Johnson                FBS (Division I-A Teams)
Rodriguez Moore                FBS (Division I-A Teams)
Zach Edwards                  FBS (Division I-A Teams)
Hosey Williams                FBS (Division I-A Teams)
Eric Wilson                    FBS (Division I-A Teams)
Chris Burrell                  FBS (Division I-A Teams)
John Lloyd                    FBS (Division I-A Teams)
Arryn Chenault                FBS (Division I-A Teams)
Rob Rice                      FBS (Division I-A Teams)
Braxton Lane                  FBS (Division I-A Teams)
Drake Bruns                  FBS (Division I-A Teams)
Andre Jones                  FBS (Division I-A Teams)
Darren Doston                FBS (Division I-A Teams)
Zach Higgenbotham            FBS (Division I-A Teams)
Solomon Tentman              FBS (Division I-A Teams)
Tim Helton                  FBS (Division I-A Teams)
Dylan Coombs                  FBS (Division I-A Teams)
Josh Russ                    FBS (Division I-A Teams)
Marcus Foster                FBS (Division I-A Teams)
Lindsay Crook                FBS (Division I-A Teams)
Mason Antoun                FBS (Division I-A Teams)
EJ Junior                  FBS (Division I-A Teams)
Kyle Nutter                FBS (Division I-A Teams)
Kevin Brown                FBS (Division I-A Teams)
Kevin Hyland                FBS (Division I-A Teams)
Jared Golden                FBS (Division I-A Teams)
Nick Temple                FBS (Division I-A Teams)
Corey Mason                FBS (Division I-A Teams)
Ey'Shawn McClain            FBS (Division I-A Teams)
Mitch Meador                FBS (Division I-A Teams)
Jon Vincent                FBS (Division I-A Teams)
Jeff Luc                  FBS (Division I-A Teams)
Anthony King              FBS (Division I-A Teams)
Alex Pace                  FBS (Division I-A Teams)
Greg Blair                FBS (Division I-A Teams)
Elijah Shuler            FBS (Division I-A Teams)
Franklin Bruscianelli      FBS (Division I-A Teams)
Andrew Gantz              FBS (Division I-A Teams)
Mark Wilson              FBS (Division I-A Teams)
Clemente Casseus          FBS (Division I-A Teams)
Sam Geraci                FBS (Division I-A Teams)
Dwight Jackson            FBS (Division I-A Teams)
Deyshawn Bond              FBS (Division I-A Teams)
Sam Longo                  FBS (Division I-A Teams)
Kirk Willis                FBS (Division I-A Teams)
Cory Keebler              FBS (Division I-A Teams)
Dan Sprague                FBS (Division I-A Teams)
Will Steur                FBS (Division I-A Teams)
Tyreek Burwell            FBS (Division I-A Teams)
Connor Donnini            FBS (Division I-A Teams)
David Niehaus            FBS (Division I-A Teams)
Kyle Williamson          FBS (Division I-A Teams)
Dominic Mainello          FBS (Division I-A Teams)
Brandon Mitchell          FBS (Division I-A Teams)
Eric Lefeld              FBS (Division I-A Teams)
Garrett Campbell          FBS (Division I-A Teams)
Ryan Leahy                FBS (Division I-A Teams)
Justin Murray            FBS (Division I-A Teams)
Kevin Schloemer          FBS (Division I-A Teams)
Austen Bujnoch           FBS (Division I-A Teams)
Parker Ehinger           FBS (Division I-A Teams)
Andre Cureton            FBS (Division I-A Teams)
Alex Chisum              FBS (Division I-A Teams)
DJ Dowdy                FBS (Division I-A Teams)
Max Morrison            FBS (Division I-A Teams)
Chris Burton            FBS (Division I-A Teams)
Nate Cole                FBS (Division I-A Teams)
Travis Johnson          FBS (Division I-A Teams)
Blake Annen              FBS (Division I-A Teams)
Jacob Giltrow          FBS (Division I-A Teams)
Javon Harrison          FBS (Division I-A Teams)
Shakim Alonzo          FBS (Division I-A Teams)
