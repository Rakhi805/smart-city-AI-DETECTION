def detect_problem(row):
    problems=[]
    if row['traffic_level']>80: problems.append('Traffic Congestion')
    if row['waste_level']>75: problems.append('Waste Overflow')
    if row['air_quality']>120: problems.append('Air Pollution')
    if row['pothole_count']>4: problems.append('Road Damage')
    return problems
