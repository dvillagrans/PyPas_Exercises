# E S C O M  -  I P N
# D A A D
# 4AV1
# Oct 15°, 2024
# @autor: Miguel Alexander Sanchez García
def run(num_pillars: int, gap_pillars: float, pillar_width: float) -> float:
    total_distance_m = (num_pillars - 1) * gap_pillars
    total_disrance_cm = total_distance_m * 100
    total_width = (num_pillars - 2) * pillar_width
    inter_distance = total_disrance_cm + total_width
    return inter_distance


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)

# Developed by MASG
