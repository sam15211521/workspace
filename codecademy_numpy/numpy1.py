import numpy as np
                        #[Lorie, Marty, Tori, Kurtz]
movie_ratings = np.array([[63.0, 54.0, 70.0, 50.0],
                          [94.0, 85.0, 89.0, 85.0],
                          [64.0, 90.0, 73.0, 85.0]])

movie_star_ratings = movie_ratings /20

tori_ratings = movie_ratings[ :,2]

marty_ratings = movie_ratings[ :, 1]
print(marty_ratings[marty_ratings > 80])

