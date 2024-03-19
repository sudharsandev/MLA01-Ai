% Define the facts
color(red).
color(blue).
color(green).
color(yellow).
color(orange).
color(purple).
color(pink).
color(brown).

fruit(apple).
fruit(banana).
fruit(grape).
fruit(orange).
fruit(peach).
fruit(plum).
fruit(strawberry).
fruit(watermelon).

% Define rules to represent the relationships between fruits and colors
fruit_color(Fruit, Color) :-
    fruit(Fruit),
    color(Color),
    fruit_color_relation(Fruit, Color).

% Define the relationships between fruits and colors
fruit_color_relation(apple, red).
fruit_color_relation(banana, yellow).
fruit_color_relation(grape, purple).
fruit_color_relation(orange, orange).
fruit_color_relation(peach, pink).
fruit_color_relation(plum, purple).
fruit_color_relation(strawberry, red).
fruit_color_relation(watermelon, green).
%fruit_color(apple, Color).
