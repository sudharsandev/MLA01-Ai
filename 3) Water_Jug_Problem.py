def water_jug_problem():
    jug1 = 0
    jug2 = 0

    jug1 = 4

    jug2 = min(jug1, 3)
    jug1-=jug2

    jug2 = 0

    jug2 = min(jug1, 3)
    jug1-=jug2

    print(f"Final State : Jug1 (4-galloon) = {jug1}, Jug2 (3-galloon) = {jug2}")

water_jug_problem()
