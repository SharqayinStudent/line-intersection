
def cross(o, a, b):
    
    return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])

# Проверка, лежат ли точки на одном отрезке
def on_segment(p, q, r):

    return min(p[0], r[0]) <= q[0] <= max(p[0], r[0]) and min(p[1], r[1]) <= q[1] <= max(p[1], r[1])


def line_intersection(p1, q1, p2, q2):
   
    
    
    o1 = cross(p1, q1, p2)
    o2 = cross(p1, q1, q2)
    o3 = cross(p2, q2, p1)
    o4 = cross(p2, q2, q1)
    

    if o1 * o2 < 0 and o3 * o4 < 0:
     
      
        denom = (q1[0] - p1[0]) * (q2[1] - p2[1]) - (q1[1] - p1[1]) * (q2[0] - p2[0])
        if denom == 0:
            return None  
    
        t1 = ((p1[0] - p2[0]) * (p2[1] - p1[1]) - (p1[1] - p2[1]) * (p2[0] - p1[0])) / denom
        return (p1[0] + t1 * (q1[0] - p1[0]), p1[1] + t1 * (q1[1] - p1[1]))
    

    if o1 == 0 and on_segment(p1, p2, q1):
        return p2
    if o2 == 0 and on_segment(p1, q2, q1):
        return q2
    if o3 == 0 and on_segment(p2, p1, q2):
        return p1
    if o4 == 0 and on_segment(p2, q1, q2):
        return q1
    

    return None

p1 = (1, 2)
q1 = (4, 1)
p2 = (1, 5)
q2 = (2, 2)

intersection = line_intersection(p1, q1, p2, q2)

if intersection:
    print("intersection")
else:
    print("Отрезки не пересекаются")
