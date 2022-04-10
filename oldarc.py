def arc(r,angle):
    arc_length = 2* math.pi * r * angle / 360
    n = int(arc_length/3)+1
    step_length = arc_length / n
    step_angle = float(angle)/ n

    for i in range(n):
        turtle.forward(step_length)
        turtle.left(step_angle)
