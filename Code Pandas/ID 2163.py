>.<

Title: Sorting Movies By Duration Time
Link: https://platform.stratascratch.com/coding/2163-sorting-movies-by-duration-time?code_type=2
Level: Easy

You have been asked to sort movies according to their duration in descending order.
Your output should contain all columns sorted by the movie duration in the given dataset.

Data movie_catalogue:
show_id: text
title: text
release_year: bigint
rating: text
duration: text

>.<

Solution:

# Import your libraries
import pandas as pd

# Start writing code

movie_catalogue = pd.DataFrame(movie_catalogue)

movie_catalogue_order = movie_catalogue.sort_values('duration',ascending=False)['title']
    
Output:

title
Show Dogs
A Champion Heart
Our House
Goosebumps 2: Haunted Halloween
Blackway
Aliens Ate My Homework
Dick Johnson Is Dead
Benchwarmers 2: Breaking Balls
YES DAY
Roped
Brain on Fire
In The Deep
He Named Me Malala
Becoming
Yoga Hosers
Be Somebody
Aliens Stole My Body
Knock Down The House
Polaroid
Incarnate
Bathtubs Over Broadway
Pup Star: World Tour
A Shaun the Sheep Movie: Farmageddon
November Criminals
Wild Oats
Vampires vs. the Bronx
Pottersville
A Cinderella Story: Christmas Wish
Dr. Seuss' The Grinch
Gnome Alone
Little Men
Open Season: Scared Silly
David Attenborough: A Life on Our Planet
Snervous Tyler Oakley
Bobbleheads The Movie
Sweetheart
SMOSH: The Movie
Echo in the Canyon
Menashe
Hope Springs Eternal
Growing Up Wild
Water & Power: A California Heist
Ghost of the Mountains
My Entire High School Sinking Into the Sea
Marvel's Hulk: Where Monsters Dwell
SPF-18
Marvel Super Hero Adventures: Frost Fight!
Star Wars: Episode VIII: The Last Jedi
Avengers: Infinity War
Solo: A Star Wars Story
Solo: A Star Wars Story (Spanish Version)
Black Panther
The Best of Enemies
The Prom
Mary Poppins Returns
Thor: Ragnarok
Greater
Jupiter Ascending
Queen of the Desert
The Zookeeper's Wife
Jingle Jangle: A Christmas Journey
Eurovision Song Contest: The Story of Fire Saga
Loving
Operation Finale
The Black Prince
The Midnight Sky
Jem and the Holograms
Marshall
Incredibles 2 (Spanish Version)
Mother's Day
Ant-Man and the Wasp
The Command
The Incredibles 2
The BFG
Selfless
Spider-Man: Into the Spider-Verse
Midnight Special
Rememory
Moxie
