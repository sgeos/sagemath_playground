# Ayres, Frank , Jr. and Elliott Mendelson. 2013. Schaum's Outlines Calculus Sixth Edition (1,105 fully solved problems, 30 problem-solving videos online). New York: McGraw Hill.
# ISBN 978-0-07-179553-1

# Chapter 4 (Circles), Question 24.
#   Let L1 and L2 be two intersecting circles determined by the equations
#     x^2 + y^2 + A1*x + B1*y + C1 = 0 and
#     x^2 + y^2 + A2*x + B2*y + C2 = 0.
#   For any number k != -1, show that
#     x^2 + y^2 + A1*x + B1*y + C1 + k * ( x^2 + y^2 + A2*x + B2*y + C2 ) = 0
#   is the equation of a circle through the intersection of points of L1 and L2.
#   Show, conversely, that every such circle may be represented by such an eqation for a suitable k.

# C2 - (C0 or C1)
# solve for x
# sub x into C2, solve for y

x, y, k = var('x y k')
a0, b0, c0 = var('a0 b0 c0')
a1, b1, c1 = var('a1 b1 c1')

# intersection

C0 = 0 == x^2 + y^2 + a0*x + b0*y + c0
C1 = 0 == x^2 + y^2 + a1*x + b1*y + c1
C2 = 0 == x^2 + y^2 + a0*x + b0*y + c0 + k * ( x^2 + y^2 + a1*x + b1*y + c1 )
I = C0 - C1
I = 0 == (a0 - a1)*x + (b0 - b1)*y + (c0 - c1)
Ix = ( ( b1 - b0 ) * y + ( c1 - c0 ) ) / ( a0 - a1 )
Iy = ( ( a1 - a0 ) * x + ( c1 - c0 ) ) / ( b0 - b1 )
# I0 = C0 - C2
# I0 = 0 == k * ( x^2 + y^2 + a1*x + b1*y + c1 )
# I1 = C1 - C2
# I1 = 0 == k * ( x^2 + y^2 + a1*x + b1*y + c1 ) + ( a0 - a1 )*x + ( b0 - b1 )*y + ( c0 - c1 )
Sx0 = 0 == x^2 + Iy^2 + a0*x + b0*Iy + c0
Sx1 = 0 == x^2 + Iy^2 + a1*x + b1*Iy + c1
Sy0 = 0 == Ix^2 + y^2 + a0*Ix + b0*y + c0
Sy1 = 0 == Ix^2 + y^2 + a1*Ix + b1*y + c1
Sx2 = 0 == x^2 + Iy^2 + a0*x + b0*Iy + c0 + k * ( x^2 + Iy^2 + a1*x + b1*Iy + c1 )
Sy2 = 0 == Ix^2 + y^2 + a0*Ix + b0*y + c0 + k * ( Ix^2 + y^2 + a1*Ix + b1*y + c1 )

Sx2 = 0 == (b0^2*(x*(a1 + x) + c1) + b1^2*(x*(a0 + x) + c0) - b0*b1*(x*(a0 + a1 + 2*x) + c0 + c1) + (a0*x - a1*x + c0 - c1)^2)*(k + 1)/(b0 - b1)^2
Sy2 = 0 == (a0^2*(y*(b1 + y) + c1) + a1^2*(y*(b0 + y) + c0) - a0*a1*(y*(b0 + b1 + 2*y) + c0 + c1) + (b0*y - b1*y + c0 - c1)^2)*(k + 1)/(a0 - a1)^2

# NEW COMPLEX ( same for Sx0~2 and Sy0~2 )
Sxa = -1/2*(a1*b0^2 - (a0 + a1)*b0*b1 + a0*b1^2 + 2*(a0 - a1)*c0 - 2*(a0 - a1)*c1 - sqrt(a1^2*b0^2 - 2*a0*a1*b0*b1 + a0^2*b1^2 + 4*(a0*a1 - a1^2 + b0*b1 - b1^2)*c0 - 4*c0^2 - 4*(a0^2 - a0*a1 + b0^2 - b0*b1 - 2*c0)*c1 - 4*c1^2)*(b0 - b1))/(a0^2 - 2*a0*a1 + a1^2 + b0^2 - 2*b0*b1 + b1^2)
Sxb = -1/2*(a1*b0^2 - (a0 + a1)*b0*b1 + a0*b1^2 + 2*(a0 - a1)*c0 - 2*(a0 - a1)*c1 + sqrt(a1^2*b0^2 - 2*a0*a1*b0*b1 + a0^2*b1^2 + 4*(a0*a1 - a1^2 + b0*b1 - b1^2)*c0 - 4*c0^2 - 4*(a0^2 - a0*a1 + b0^2 - b0*b1 - 2*c0)*c1 - 4*c1^2)*(b0 - b1))/(a0^2 - 2*a0*a1 + a1^2 + b0^2 - 2*b0*b1 + b1^2)
Sya = 1/2*((a0*a1 - a1^2)*b0 - (a0^2 - a0*a1)*b1 - 2*(b0 - b1)*c0 + 2*(b0 - b1)*c1 - sqrt(a1^2*b0^2 - 2*a0*a1*b0*b1 + a0^2*b1^2 + 4*(a0*a1 - a1^2 + b0*b1 - b1^2)*c0 - 4*c0^2 - 4*(a0^2 - a0*a1 + b0^2 - b0*b1 - 2*c0)*c1 - 4*c1^2)*(a0 - a1))/(a0^2 - 2*a0*a1 + a1^2 + b0^2 - 2*b0*b1 + b1^2)
Syb = 1/2*((a0*a1 - a1^2)*b0 - (a0^2 - a0*a1)*b1 - 2*(b0 - b1)*c0 + 2*(b0 - b1)*c1 + sqrt(a1^2*b0^2 - 2*a0*a1*b0*b1 + a0^2*b1^2 + 4*(a0*a1 - a1^2 + b0*b1 - b1^2)*c0 - 4*c0^2 - 4*(a0^2 - a0*a1 + b0^2 - b0*b1 - 2*c0)*c1 - 4*c1^2)*(a0 - a1))/(a0^2 - 2*a0*a1 + a1^2 + b0^2 - 2*b0*b1 + b1^2)

# NEW SIMPLIFIED
Sxa = ( (a0 - a1)*(c1 - c0) - (b0 - b1)*((a1*b0 - a0*b1)/2 - sqrt( (a1*b0 - a0*b1)^2/4 + (a0 - a1)*(a1*c0 - a0*c1) + (b0 - b1)*(b1*c0 - b0*c1) - (c0 - c1)^2 ))) / ( ( a0 - a1 )^2 + ( b0 - b1 )^2 )
Sxb = ( (a0 - a1)*(c1 - c0) - (b0 - b1)*((a1*b0 - a0*b1)/2 + sqrt( (a1*b0 - a0*b1)^2/4 + (a0 - a1)*(a1*c0 - a0*c1) + (b0 - b1)*(b1*c0 - b0*c1) - (c0 - c1)^2 ))) / ( ( a0 - a1 )^2 + ( b0 - b1 )^2 )
Sya = ( (b0 - b1)*(c1 - c0) - (a0 - a1)*((a0*b1 - a1*b0)/2 + sqrt( (a1*b0 - a0*b1)^2/4 + (a0 - a1)*(a1*c0 - a0*c1) + (b0 - b1)*(b1*c0 - b0*c1) - (c0 - c1)^2 ))) / ( ( a0 - a1 )^2 + ( b0 - b1 )^2 )
Syb = ( (b0 - b1)*(c1 - c0) - (a0 - a1)*((a0*b1 - a1*b0)/2 - sqrt( (a1*b0 - a0*b1)^2/4 + (a0 - a1)*(a1*c0 - a0*c1) + (b0 - b1)*(b1*c0 - b0*c1) - (c0 - c1)^2 ))) / ( ( a0 - a1 )^2 + ( b0 - b1 )^2 )

(a0 - a1)*(a1*c0 - a0*c1) + (b0 - b1)*(b1*c0 - b0*c1)
  == c0*(a1*(a0 - a1) + b1*(b0 - b1)) + c1*(a0*(a1 - a0) - b0*(b0 + b1))
  == a1*c0*(a0 - a1) - a0*c1*(a0 - a1) + b1*c0*(b0 - b1) - b0*c1*(b0 + b1)
  == c0*(a1*(a0 - a1) + b1*(b0 - b1)) - c1*(a0*(a0 - a1) - b0*(b0 + b1))

# OLD
Sxa = (a0*(b1*(b0 - b1) - 2*(c0 - c1)) - a1*(b0*(b0 - b1) - 2*(c0 - c1)) + (b0 - b1)*sqrt(a0^2*(b1^2 - 4*c1) + a0*a1*(4*(c0 + c1) - 2*b0*b1) + a1^2*(b0^2 - 4*c0) - 4*(b0^2*c1 - b0*b1*(c0 + c1) + b1^2*c0 + (c0 - c1)^2))) / ( 2 * ( ( a0 - a1 )^2 + ( b0 - b1 )^2 ) )
Sxb = (a0*(b1*(b0 - b1) - 2*(c0 - c1)) - a1*(b0*(b0 - b1) - 2*(c0 - c1)) - (b0 - b1)*sqrt(a0^2*(b1^2 - 4*c1) + a0*a1*(4*(c0 + c1) - 2*b0*b1) + a1^2*(b0^2 - 4*c0) - 4*(b0^2*c1 - b0*b1*(c0 + c1) + b1^2*c0 + (c0 - c1)^2))) / ( 2 * ( ( a0 - a1 )^2 + ( b0 - b1 )^2 ) )
Sya = (a0^2*(-b1) + a0*a1*(b0 + b1) - a1^2*b0 - 2*(b0 - b1)*(c0 - c1) + (a0 - a1)*sqrt(a0^2*(b1^2 - 4*c1) + a0*a1*(4*(c0 + c1) - 2*b0*b1) + a1^2*(b0^2 - 4*c0) - 4*(b0^2*c1 - b0*b1*(c0 + c1) + b1^2*c0 + (c0 - c1)^2))) / ( 2 * ( ( a0 - a1 )^2 + ( b0 - b1 )^2 ) )
Syb = (a0^2*(-b1) + a0*a1*(b0 + b1) - a1^2*b0 - 2*(b0 - b1)*(c0 - c1) - (a0 - a1)*sqrt(a0^2*(b1^2 - 4*c1) + a0*a1*(4*(c0 + c1) - 2*b0*b1) + a1^2*(b0^2 - 4*c0) - 4*(b0^2*c1 - b0*b1*(c0 + c1) + b1^2*c0 + (c0 - c1)^2))) / ( 2 * ( ( a0 - a1 )^2 + ( b0 - b1 )^2 ) )

solve multiple equations

# Reference:
#   "Intersection of Two Circles"
#   http://paulbourke.net/geometry/circlesphere/

# x^2 + y^2 + a0*x + b0*y + c0 = 0
#
#                  _P3A_
#       R0   _  /    |  \_  R1
#      _  /          |H   \_
#   /       W0       |  W1  \
# P0--------------- P2 ------ P1
#   ------------------------- 
#   \  _         D   |     _/
#         \  _       |H  _/
#       R0      \  _ | _/   R1
#                   P3B
#
#        x^2 + y^2 + a1*x + b1*y + c1 = 0


x = var('x')
y = var('y')

a0 = var('a0')
b0 = var('b0')
c0 = var('c0')

a1 = var('a1')
b1 = var('b1')
c1 = var('c1')

P0x = -a0 / 2
P0y = -b0 / 2
P1x = -a1 / 2
P1y = -b1 / 2

D = sqrt( (P1x - P0x)^2 + (P1y - P0y)^2 )
R0 = sqrt( a0^2 + b0^2 - 4*c0 ) / 2
R1 = sqrt( a1^2 + b1^2 - 4*c1 ) / 2
W0 = ( R0^2 - R1^2 + D^2 ) / ( 2*D )
W1 = ( R1^2 - R0^2 + D^2 ) / ( 2*D )
H = R0^2 - W0^2 # H = R1^2 - W1^2

P2x = P0x + W0 * ( P1x - P0x ) / D
P2y = P0y + W0 * ( P1y - P0y ) / D
P3xo = H * ( P1y - P0y ) / D
P3yo = H * ( P1x - P0x ) / D

P3Ax = P2x + P3xo
P3Ay = P2y - P3yo
P3Bx = P2x - P3xo
P3By = P2y + P3yo

# simplified

P0x = -a0 / 2 # OK
P0y = -b0 / 2 # OK
P1x = -a1 / 2 # OK
P1y = -b1 / 2 # OK

D = sqrt( ( a0 - a1 )^2 + ( b0 - b1 )^2 ) / 2 # OK
R0 = sqrt( a0^2 + b0^2 - 4*c0 ) / 2 # OK
R1 = sqrt( a1^2 + b1^2 - 4*c1 ) / 2 # OK
W0 = ( a0 * (a0 - a1) + b0 * (b0 - b1) + 2 * (c1 - c0) ) / ( 2 * sqrt( ( a0 - a1 )^2 + ( b0 - b1 )^2 ) ) # OK
W1 = ( a1 * (a1 - a0) + b1 * (b1 - b0) + 2 * (c0 - c1) ) / ( 2 * sqrt( ( a0 - a1 )^2 + ( b0 - b1 )^2 ) ) # OK
H = ( a0^2*(b1^2 - 4*c1) + a0*a1*( 4*(c0 + c1) - 2*b0*b1) + a1^2*(b0^2 - 4*c0) - 4*(b0^2*c1 - b0*b1*(c0 + c1) + b1^2*c0 + (c0 - c1)^2) ) / ( 4 * ( ( a0 - a1 )^2 + ( b0 - b1 )^2 ) ) # OK

P2x = ( a0*( b1*(b0 - b1) + 2*(c1 - c0) ) + a1*( b0*(b1 - b0) + 2*(c0 - c1) ) ) / ( 2 * ( ( a0 - a1 )^2 + ( b0 - b1 )^2 ) ) # OK
P2y = ( (a0 - a1)*(a1*b0 - a0*b1) - 2*(b0 - b1)*(c0 - c1) ) / ( 2 * ( ( a0 - a1 )^2 + ( b0 - b1 )^2 ) ) # OK
P3xo = (1/4)*(b0-b1)*(a0^2*(b1^2 - 4*c1) + a0*a1*(4*(c0 + c1) - 2*b0*b1) + a1^2*(b0^2 - 4*c0) - 4*(b0^2*c1 - b0*b1*(c0 + c1) + b1^2*c0 + (c0 - c1)^2)) / ( (a0 - a1)^2 + (b0 - b1)^2 )^(3/2) # OK
P3yo = (1/4)*(a0-a1)*(a0^2*(b1^2 - 4*c1) + a0*a1*(4*(c0 + c1) - 2*b0*b1) + a1^2*(b0^2 - 4*c0) - 4*(b0^2*c1 - b0*b1*(c0 + c1) + b1^2*c0 + (c0 - c1)^2)) / ( (a0 - a1)^2 + (b0 - b1)^2 )^(3/2) # OK


P2x = ( a0*( b1*(b0 - b1) + 2*(c1 - c0) ) + a1*( b0*(b1 - b0) + 2*(c0 - c1) ) ) / ( 2 * ( ( a0 - a1 )^2 + ( b0 - b1 )^2 ) ) # OK
P2y = ( (a0 - a1)*(a1*b0 - a0*b1) - 2*(b0 - b1)*(c0 - c1) ) / ( 2 * ( ( a0 - a1 )^2 + ( b0 - b1 )^2 ) ) # OK

P2x = (a0 - a1)*(a0*(a0 - a1) + b0*(b0 - b1) + 2*(c1 - c0)) - a0*((a0 - a1)^2 + (b0 - b1)^2) / ( 2 * ( ( a0 - a1 )^2 + ( b0 - b1 )^2 ) ) # OK
P2y = (b0 - b1)*(a0*(a0 - a1) + b0*(b0 - b1) + 2*(c1 - c0)) - a0*((a0 - a1)^2 + (b0 - b1)^2) / ( 2 * ( ( a0 - a1 )^2 + ( b0 - b1 )^2 ) ) # OK

P3Ax =
1/8 *
(
a1^2*b0^3 - a0^2*b1^3 - (2*a0*a1 + a1^2)*b0^2*b1 + (a0^2 + 2*a0*a1)*b0*b1^2
- 4*(
(b0 - b1)*((1/2)*(a1*b0 - a0*b1)*sqrt((a0 - a1)^2 + (b0 - b1)^2) + c0^2 + c1^2)
+ c0*((a0 - a1)*sqrt((a0 - a1)^2 + (b0 - b1)^2) + a1*b0*(a1 - a0) + a1*b1*(a0 - a1) - b0^2*b1 + 2*b0*b1^2 - b1^3)
+ c1*(-b1*(a0^2 - a0*a1 + 2*b0^2) + (a1 - a0)*sqrt((a0 - a1)^2 + (b0 - b1)^2) + a0*b0*(a0 - a1) + b0^3 + b0*b1^2 + 2*c0*(b1 - b0))
)
)
/ ( (1/2) * ( (a0 - a1)^2 + (b0 - b1)^2 )^(3/2) )

