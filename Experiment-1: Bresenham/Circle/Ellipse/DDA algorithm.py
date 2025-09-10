#1.a.Bresenham algorithm
import matplotlib.pyplot as plt

def plot_point(x, y):
    plt.plot(x, y, 'bo')

def bresenham_line(x1, y1, x2, y2):
    dx = abs(x2 - x1)
    dy = abs(y2 - y1)
    x, y = x1, y1
    sx = 1 if x2 > x1 else -1
    sy = 1 if y2 > y1 else -1

    if dx > dy:
        err = dx / 2.0
        while x != x2:
            plot_point(x, y)
            err -= dy
            if err < 0:
                y += sy
                err += dx
            x += sx
    else:
        err = dy / 2.0
        while y != y2:
            plot_point(x, y)
            err -= dx
            if err < 0:
                x += sx
                err += dy
            y += sy
    plot_point(x, y)

def midpoint_circle(xc, yc, r):
    x = 0
    y = r
    p = 1 - r
    while x <= y:
        for a, b in [(x, y), (y, x), (-x, y), (-y, x), (-x, -y), (-y, -x), (x, -y), (y, -x)]:
            plot_point(xc + a, yc + b)
        x += 1
        if p < 0:
            p += 2 * x + 1
        else:
            y -= 1
            p += 2 * (x - y) + 1

plt.figure(figsize=(6, 6))
plt.axis('equal')
plt.grid(True)

bresenham_line(2, 2, 20, 10)
midpoint_circle(10, 10, 8)

plt.title("Bresenham Line and Midpoint Circle")
plt.show()

#1.b.Midpoint Circle Algorithm

import matplotlib.pyplot as plt

x0=int(input("Enter x0:"))
y0=int(input("Enter y0:"))
r=int(input("Enter Radius:"))

p = 1 - r

x=0
y=r

x_points=[]
y_points=[]

x_points.extend([x+x0,x+x0,-x+x0,-x+x0,y+x0,y+x0,-y+x0,-y+x0])
    
y_points.extend([y+y0,-y+y0,y+y0,-y+y0,x+y0,-x+y0,x+y0,-x+y0])

while(x<y):
    if(p<0):
        p=p+(2*(x+1))+1
        x=x+1
    else:
        p=p+(2*(x+1))+1-(2*(y-1))
        x=x+1
        y=y-1
        
    x_points.extend([x+x0,x+x0,-x+x0,-x+x0,y+x0,y+x0,-y+x0,-y+x0])
    
    y_points.extend([y+y0,-y+y0,y+y0,-y+y0,x+y0,-x+y0,x+y0,-x+y0])
    
    #print("(",x,",",y,")")



plt.plot(x_points,y_points,'s')
plt.plot(x0,y0,'ro')
plt.title("Midpoint Circle Algorithm")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.grid(True)
plt.show()

#1.c.DDA algorithm
import matplotlib.pyplot as plt

x0 = int(input("Enter x0: "))
y0 = int(input("Enter y0: "))
x1 = int(input("Enter x1: "))
y1 = int(input("Enter y1: "))

dx = x1 - x0
dy = y1 - y0
steps = max(abs(dx), abs(dy))
x_inc = dx / steps
y_inc = dy / steps

x = x0
y = y0

x_points = []
y_points = []

for i in range(steps + 1):
    x_points.append(round(x))
    y_points.append(round(y))
    x += x_inc
    y += y_inc

plt.plot(x_points, y_points, marker='o')
plt.title("Line drawn using DDA Algorithm")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.grid(True)
plt.show()

#1.d.Midpoint ellipse algorithm
import matplotlib.pyplot as plt

rx = int(input("Enter the radius along x: "))
ry = int(input("Enter the radius along y: "))

x = 0
y = ry

p1 = (ry**2) + (0.25 * (rx**2)) - ((rx**2) * ry)

while (2 * (ry**2) * x <= 2 * (rx**2) * y):
    plt.plot(x, y, marker='o', color='red')
    plt.plot(-x, y, marker='o', color='red')
    plt.plot(x, -y, marker='o', color='red')
    plt.plot(-x, -y, marker='o', color='red')

    if p1 < 0:
        x += 1
        p1 = p1 + (2 * (ry**2) * x) + (ry**2)
    else:
        x += 1
        y -= 1
        p1 = p1 + (2 * (ry**2) * x) - (2 * (rx**2) * y) + (ry**2)

p2 = (ry**2) * ((x + 0.5)**2) + ((rx**2) * ((y - 1)**2)) - ((rx**2) * (ry**2))

while y >= 0:
    plt.plot(x, y, marker='o', color='red')
    plt.plot(-x, y, marker='o', color='red')
    plt.plot(x, -y, marker='o', color='red')
    plt.plot(-x, -y, marker='o', color='red')

    if p2 > 0:
        y -= 1
        p2 = p2 - (2 * (rx**2) * y) + (rx**2)
    else:
        x += 1
        y -= 1
        p2 = p2 + (2 * (ry**2) * x) - (2 * (rx**2) * y) + (rx**2)

plt.title("Ellipse drawn using Midpoint Ellipse Algorithm")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.grid(True)
plt.gca().set_aspect('equal', adjustable='box')
plt.show()

# x_points.extend([x+x0,x+x0,-x+x0,-x+x0,y+x0,y+x0,-y+x0,-y+x0])
    
# y_points.extend([y+y0,-y+y0,y+y0,-y+y0,x+y0,-x+y0,x+y0,-x+y0])
