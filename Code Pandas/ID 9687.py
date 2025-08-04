>.<

Title: Find details of oscar winners between 2001 and 2009
Link: https://platform.stratascratch.com/coding/9687-find-details-of-oscar-winners-between-2001-and-2009?code_type=2
Level: Easy

Find the details of oscar winners between 2001 and 2009.

Data oscar_nominees:
year: bigint
category: text 
nominee: text
movie: text
winner: tinyint
id: bigint

>.<

Solution:

# Import your libraries
import pandas as pd

# Start writing code

oscar_nominees = pd.DataFrame(oscar_nominees)

oscar_nominees_winner = oscar_nominees[(oscar_nominees['winner'] == 1) & (oscar_nominees['year'].between(2001,2009))]['nominee']
    
Output:

nominee
Adrien Brody
Alan Arkin
Cate Blanchett
Catherine Zeta-Jones
Charlize Theron
Chris Cooper
Christoph Waltz
Daniel Day-Lewis
Denzel Washington
Forest Whitaker
George Clooney
Halle Berry
Heath Ledger
Helen Mirren
Hilary Swank
Jamie Foxx
Javier Bardem
Jeff Bridges
Jennifer Connelly
Jennifer Hudson
Jim Broadbent
Kate Winslet
Marion Cotillard
Mo'Nique
Morgan Freeman
Nicole Kidman
Pen_lope Cruz
Philip Seymour Hoffman
Rachel Weisz
Reese Witherspoon
Ren_e Zellweger
Sandra Bullock
Sean Penn
Sean Penn
Tilda Swinton
Tim Robbins
