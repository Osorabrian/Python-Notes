import turtle # importing turtle module

t = turtle.Turtle() #creating a turtle

#using a turtle to draw a square
def square(sides, distance):
	for i in range(sides):
		t.fd(distance)
		t.lt(90)

# square(4, 100)

#using a turtle to draw a polygon
def polygon(sides, distance):
	angle = 360/sides
	for i in range(sides):
		t.fd(distance)
		t.lt(angle)

# polygon(6, 100)

#using a turtle to draw a circle
def circle(sides, distance):
	angle = 360/sides
	for i in range(sides):
		t.fd(distance/sides)
		t.lt(angle)

# circle(20, 210)

#using a turtle to draw a star
def star(polygon_sides, star_sides = 2, distance = 150, star_angle = 120):
	polygon_angle = 360/polygon_sides
	next_star_angle = star_angle + polygon_angle
	for n in range(polygon_sides):
		for i in range(star_sides):
				t.lt(star_angle)
				t.fd(distance)
		t.lt(next_star_angle)

star(polygon_sides = 8)

#this clears the screen
t.clear()

#this command resets the screen
turtle.resetscreen()
turtle.mainloop()