import fresh_tomatoes
import media

# Movie Information
# Store movie title, description, image link, trailer link, release date, and phase
""" Phase One """

ironman = media.Movie("Iron Man",
    "Billionaire industrialist Tony Stark builds himself a "
    "suit of armor after he is taken captive by a terrorist "
    "organization. Free from his captors, he decides to upgrade "
    "and don his armor as Iron Man in order to hunt down weapons "
    "that were sold under the table.",
    "https://upload.wikimedia.org/wikipedia/en/7/70/Ironmanposter.JPG",
    "https://youtu.be/8hYlB38asDY",
    "May 2, 2008",
    "Phase One: Avengers Assembled",
    "p1")

hulk = media.Movie("The Incredible Hulk",
    "After being exposed to gamma radiation that causes him to "
    "transform into the monstrous Hulk, scientist Bruce Banner "
    "goes on the run and isolates himself from his love, Betty "
    "Ross. Hunted by the military, Banner seeks to cure himself "
    "and prevent his condition from being weaponized.",
    "https://upload.wikimedia.org/wikipedia/en/8/88/The_Incredible_Hulk_poster.jpg",
    "https://youtu.be/xbqNb2PFKKA",
    "June 13, 2008",
    "Phase One: Avengers Assembled",
    "p1")

ironman2 = media.Movie("Iron Man 2",
    "After Tony Stark reveals himself to be Iron Man, the U.S. "
    "government demands he hand over his technology. Meanwhile, "
    "a rival industrialist and a Russian scientist conspire to use "
    "his own technology against him.",
    "https://upload.wikimedia.org/wikipedia/en/e/ed/Iron_Man_2_poster.jpg",
    "https://www.youtube.com/watch?v=BoohRoVA9WQ",
    "May 7, 2010",
    "Phase One: Avengers Assembled",
    "p1")

thor = media.Movie("Thor",
    "Thor, crown prince of Asgard, is banished to Earth and stripped "
    "of his powers after he reignites a dormant war. As his brother, "
    "Loki, plots to take the throne for himself, Thor must prove "
    "himself worthy and reclaim his hammer Mjolnir.",
    "https://upload.wikimedia.org/wikipedia/en/f/fc/Thor_poster.jpg",
    "https://www.youtube.com/watch?v=JOddp-nlNvQ",
    "May 6, 2011",
    "Phase One: Avengers Assembled",
    "p1")

captainamerica = media.Movie("Captain America: The First Avenger",
    "In 1942, Steve Rogers is deemed physically unfit to enlist in "
    "the U.S. Army and fight the Nazis in World War II. Recruited for "
    "a secret military operation, he is physically transformed into a "
    "super-soldier dubbed Captain America and must battle the Red Skull, "
    "head of a Nazi weaponry division known as Hydra.",
    "https://upload.wikimedia.org/wikipedia/en/3/37/Captain_America_The_First_Avenger_poster.jpg",
    "https://www.youtube.com/watch?v=JerVrbLldXw",
    "July 22, 2011",
    "Phase One: Avengers Assembled",
    "p1")

avengers = media.Movie("Marvel's The Avengers",
    "Nick Fury, the director of S.H.I.E.L.D., gathers the superheroes "
    "Iron Man, Thor, Captain America, the Hulk, Black Widow and Hawkeye "
    "to fight Thor's brother Loki, who plots to subjugate the Earth.",
    "https://upload.wikimedia.org/wikipedia/en/f/f9/TheAvengers2012Poster.jpg",
    "https://www.youtube.com/watch?v=eOrNdBpGMv8",
    "May 4, 2012",
    "Phase One: Avengers Assembled",
    "p1")

""" Phase Two """

ironman3 = media.Movie("Iron Man 3",
    "Tony Stark faces a powerful enemy, the Mandarin, who attacks "
    "and destroys his mansion. Left to his own devices and battling "
    "posttraumatic stress disorder, Stark struggles to get to the "
    "bottom of a series of mysterious explosions.",
    "https://upload.wikimedia.org/wikipedia/en/d/d5/Iron_Man_3_theatrical_poster.jpg",
    "https://www.youtube.com/watch?v=oYSD2VQagc4",
    "May 3, 2013",
    "Phase Two",
    "p2")

thor2 = media.Movie("Thor: The Dark World",
    "Thor reunites with astrophysicist Jane Foster as a series of "
    "portals, linking worlds at random, begin to appear. He discovers "
    "that Malekith and his army of Dark Elves have returned after "
    "thousands of years, and they seek a powerful weapon known as the Aether. "
    "Thor must join forces with his now-imprisoned brother Loki to stop them.",
    "https://upload.wikimedia.org/wikipedia/en/7/7e/Thor_-_The_Dark_World_poster.jpg",
    "https://www.youtube.com/watch?v=npvJ9FTgZbM",
    "November 8, 2013",
    "Phase Two",
    "p2")

captainamerica2 = media.Movie("Captian America: The Winter Soldier",
    "Steve Rogers, now working with S.H.I.E.L.D., teams up with Natasha "
    "Romanoff / Black Widow and Sam Wilson / Falcon to expose a deep "
    "conspiracy which involves a mysterious assassin known only as the "
    "Winter Soldier.",
    "https://upload.wikimedia.org/wikipedia/en/e/e8/Captain_America_The_Winter_Soldier.jpg",
    "https://www.youtube.com/watch?v=7SlILk2WMTI",
    "April 4, 2014",
    "Phase Two",
    "p2")

gotg = media.Movie("Guardians of the Galaxy",
    "Peter Quill / Star-Lord and a group of misfits, including Gamora, "
    "Rocket, Drax the Destroyer and Groot, fight to keep a powerful orb "
    "from the clutches of the villainous Ronan.",
    "https://upload.wikimedia.org/wikipedia/en/8/8f/GOTG-poster.jpg",
    "https://www.youtube.com/watch?v=d96cjJhvlMA",
    "August 1, 2014",
    "Phase Two",
    "p2")

avengers2 = media.Movie("Avengers: Age of Ultron",
    "Iron Man, Captain America, Thor, the Hulk, Black Widow, and Hawkeye "
    "must work together as the Avengers to defeat Ultron, a technological "
    "enemy bent on human extinction, while encountering the powerful twins "
    "Pietro and Wanda Maximoff, as well as the new entity Vision.",
    "https://upload.wikimedia.org/wikipedia/en/1/1b/Avengers_Age_of_Ultron.jpg",
    "https://www.youtube.com/watch?v=tmeOjFno6Do",
    "May 1, 2015",
    "Phase Two",
    "p2")

antman = media.Movie("Ant-Man",
    "Thief Scott Lang must aid his mentor Dr. Hank Pym in safeguarding the "
    "mystery of the Ant-Man technology, which allows its user to decrease in "
    "size but increase in strength, from various menaces and plot a heist to "
    "defend the Earth.",
    "https://upload.wikimedia.org/wikipedia/en/7/75/Ant-Man_poster.jpg",
    "https://www.youtube.com/watch?v=pWdKf3MneyI",
    "July 17, 2015",
    "Phase Two",
    "p2")

""" Phase Three """

captainamerica3 = media.Movie("Captain America: Civil War",
    "The Avengers become fractured into two opposing teams, one led by Captain "
    "America and another by Iron Man, after extensive collateral damage prompts "
    "politicians to pass an act regulating superhuman activity with government "
    "oversight and accountability for the Avengers while also facing against a "
    "new enemy, Helmut Zemo, who seeks revenge upon the Avengers.",
    "https://upload.wikimedia.org/wikipedia/en/5/53/Captain_America_Civil_War_poster.jpg",
    "https://www.youtube.com/watch?v=dKrVegVI0Us",
    "May 6, 2016",
    "Phase Three",
    "p3")

doctorstrange = media.Movie("Doctor Strange",
    "After Stephen Strange, the world's top neurosurgeon, is involved in a car "
    "accident that ruins his career, he sets out on a journey of healing, where "
    "he encounters the Ancient One, who teaches Strange the use of Mystic Arts and "
    "to defend the Earth from mystical threats.",
    "https://upload.wikimedia.org/wikipedia/en/c/c7/Doctor_Strange_poster.jpg",
    "https://www.youtube.com/watch?v=Lt-U_t2pUHI",
    "November 4, 2016",
    "Phase Three",
    "p3")

gotg2 = media.Movie("Guardians of the Galaxy Vol. 2",
    "The Guardians of the Galaxy travel throughout the cosmos and struggle to keep "
    "their newfound family together while helping Peter Quill learn more about his "
    "true parentage and facing against new enemies.",
    "https://upload.wikimedia.org/wikipedia/en/9/95/GotG_Vol2_poster.jpg",
    "https://www.youtube.com/watch?v=dW1BIid8Osg",
    "May 5, 2017",
    "Phase Three",
    "p3")

spiderman = media.Movie("Spider-Man: Homecoming",
    "Peter Parker tries to balance being the hero Spider-Man with his high school "
    "life under guidance of Tony Stark as he deals with the threat of the Vulture.",
    "https://upload.wikimedia.org/wikipedia/en/f/f9/Spider-Man_Homecoming_poster.jpg",
    "https://www.youtube.com/watch?v=n9DwoQ7HWvI",
    "July 7, 2017",
    "Phase Three",
    "p3")

""" Future """

thor3 = media.Movie("Thor: Ragnorak",
    "After the events of Avengers: Age of Ultron, and four years after the events of "
    "Thor: The Dark World, Thor, held captive on the planet Sakaar without his "
    "hammer Mjolnir, must win a gladiatorial duel against an old friend-the Hulk-in "
    "order to return to Asgard in time to stop the villainous Hela and the "
    "impending Ragnarok, the doom of the Asgardian civilization.",
    "https://upload.wikimedia.org/wikipedia/en/7/7d/Thor_Ragnarok_poster.jpg",
    "https://www.youtube.com/watch?v=ue80QwXMRHg",
    "November 3, 2017",
    "Future Film",
    "p4")

blackpanther = media.Movie("Black Panther",
    "After the events of Captain America: Civil War, King T'Challa returns home to "
    "Wakanda. He soon finds his sovereignty challenged by factions within his own "
    "country. When two enemies conspire to bring down the kingdom, T'Challa must team "
    "up, as the Black Panther, with C.I.A. agent Everett K. Ross and members of the "
    "Dora Milaje-Wakanda's special forces-to prevent a world war.",
    "https://upload.wikimedia.org/wikipedia/en/0/0c/Black_Panther_film_poster.jpg",
    "https://www.youtube.com/watch?v=dxWvtMOGAhw",
    "February 16, 2018",
    "Future Film",
    "p4")


# List Films
movies = [ironman, hulk, ironman2, thor, captainamerica, avengers, ironman3, thor2,
captainamerica2, gotg, avengers2, antman, captainamerica3, doctorstrange, gotg2, spiderman,
thor3, blackpanther]

fresh_tomatoes.open_movies_page(movies)
