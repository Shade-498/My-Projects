import turtle
import colorsys

t = turtle.Turtle()
screen = turtle.Screen().bgcolor('black')
t.shape('')

t.speed(0)

n = 70
h = 0

for i in range (360):
  color = colorsys.hsv_to_rgb(h, 1, 0.8)
  h+= 1/n

  t.color(color)
  t.left(1)
  t.fd(1)
  for i in range(2):
    t.left(2)
    t.circle(100)