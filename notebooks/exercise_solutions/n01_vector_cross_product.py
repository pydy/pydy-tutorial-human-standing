p1 = 23 * N.x - 12 * N.y
p2 = 16 * N.x + 2 * N.y - 4 * N.z
p3 = N.x + 14 * N.z

cross(p2 - p1, p3 - p1).magnitude() / 2
