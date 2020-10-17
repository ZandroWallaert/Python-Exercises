"""
Program the turtle to draw Koch's snowflake.
**Hint:** Lookup the Lindenmayer system and use this to rewrite a string with "commando's".
"""
import turtle

# Draw a Koch snowflake
import turtle
import math

wn = turtle.Screen()
wx = wn.window_width()*.5
wh = wn.window_height()*.5
base_triangle_length = 2.0/math.sqrt(3.0)*wh

depth = 2

Koch = turtle.Turtle()
Koch.speed(50*(depth+1))
Koch.penup()
Koch.setposition((-wx/2,-wh/2))
Koch.pendown()
Koch.left(60)

def draw_koch_segment(t, run, mydepth, depth):
  if mydepth == depth:
    t.fd(run)
  else:
    myrun = run/3.0
    draw_koch_segment(t, myrun, mydepth+1, depth)
    t.left(60)
    draw_koch_segment(t, myrun, mydepth+1, depth)
    t.right(120)
    draw_koch_segment(t, myrun, mydepth+1, depth)
    t.left(60)
    draw_koch_segment(t, myrun, mydepth+1, depth)
for ii in range(3):
  draw_koch_segment(Koch, base_triangle_length, 0, depth)
  Koch.right(120)


