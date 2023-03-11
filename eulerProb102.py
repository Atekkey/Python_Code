#SOLVED
import math
def getPhi(A, B):
    dot = A[0] * B[0] + A[1] * B[1]
    magA = (A[0]**2 + A[1]**2) ** 0.5
    magB = (B[0]**2 + B[1]**2) ** 0.5
    phi = 180 * math.acos(dot / (magA * magB)) / math.pi
    return phi
def main():
    fileName = 'p102_triangles.txt'
    file = open(fileName,'r')
    lines = file.readlines()
    file.close()
    for j in range(len(lines)):
        lines[j] = list(lines[j].strip("\n").split(","))
    isTsum = 0
    for i in range(1000):
        A = (int(lines[i][0]), int(lines[i][1]))
        B = (int(lines[i][2]), int(lines[i][3]))
        C = (int(lines[i][4]), int(lines[i][5]))
        phi1 = getPhi(A, B)
        phi2 = getPhi(B, C)
        phi3 = getPhi(A, C)
        if(phi1+phi3 > 180 and phi2+phi3 > 180 and phi1+phi2 > 180):
            isTsum +=1
    return isTsum
print(main())
"""Method, used A dot B = |A||B|cos(phi) ABC are each vectors from origin to points abc. 
If the angles of ABC are all under 180 degr then the point (0,0) must be looking at all verticies
with an angle of less than 180. Therefore if angles of ABC < 180, then (0,0) must be onlooking
FROM OUTSIDE the triangle.
If any two angles add up to >180, the origin must be inside the triangle
"""