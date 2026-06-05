draw = input("""
             
do u want a star or something like that
enter on;y in lower case : """)
if (draw == "yes"):
    num1 = int(input("enter the length : "))
    num2 = int(input("enter the width : "))
    sonic = int(input("enter a the number (speed) : "))
    puma = int(input("enter the anout of times it should repeat (more higher is better) : "))
    import turtle

pen = turtle.Turtle()
pen.speed(sonic)
for i in range(puma):
    pen.forward(num1)  # length of side
    pen.right(num2)     # turn right 90 degrees
turtle.done()


