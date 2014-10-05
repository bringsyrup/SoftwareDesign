#random trippy art generator
makes weird random trippy art.

##known bugs
sometimes you'll get an arror that looks like this:

```sh
Traceback (most recent call last):
  File "./art.py", line 151, in <module>
    map_colors(1)
  File "./art.py", line 98, in map_colors
    res_grid0 = evaluate(func0, xg, yg)
  File "./art.py", line 87, in evaluate
    exec function
  File "<string>", line 1, in <module>
TypeError: 'numpy.ndarray' object is not callable
```

but this only occurs occasionally and I don't know why, seeing as I ALWAYS call evaluate with a numpy.ndarray. Always. And only sometimes does it complain.
it could be that the random function generator occasionally produces an invalid function. but it's just art, so I don't feel the need to fix it. sometimes artwork just doesn't work out, ya know? sometimes all the paint turns brown and the paintbrushes are all dry and you're out of turpenoid you gotta start over with a blank canvas. 

##some things that are different about my code vs. the instructions give.

so first, I never read any of the instructions, I just read enough to understand what we were supposed to produce: randomly generated art from random functions.
my random function gnerator spits out a string written in mathematically correct terms (for example, the logic in the function generator prevents a variable or number from coming directly after an end parentheses and will add a random operand where appropriate), and then I execute the string function in another function, so any single function can be called multiple times for different color channels, or you can generate different functions for each color channel, which produces more colorful images.

##getting interesting art
the art is more interesting if the functions are dynamic within the x and y ranges set in the code. so for a small range, like -10 < x,y < 10 the functions work out well if they are dynamic in a small range. 

