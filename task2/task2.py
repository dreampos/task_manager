import sys

def check_point_inside_circle(point_coords, circle_center_coords, circle_radius):

    cond_ex = (point_coords[0] - circle_center_coords[0]) ** 2 + (point_coords[1] + circle_center_coords[1]) ** 2
    if cond_ex < circle_radius ** 2:
        return 1
    elif cond_ex == circle_radius ** 2:
        return 0
    else:
        return 2

def main():

    with open(sys.argv[1], "r") as center_info_file:
        with open(sys.argv[2], "r") as points_info_file:

            circle_center_info = center_info_file.read().strip().split('\n')
            circle_center_coords = list(map(float, circle_center_info[0].split()))
            circle_radius = float(circle_center_info[1])

            points_info = points_info_file.read().strip().split('\n')

            if len(points_info) >= 1:
                for point_coords in points_info[: min(100, len(points_info))]:
                    point_coords_float = list(map(float, point_coords.split()))

                    print(check_point_inside_circle(point_coords_float, circle_center_coords, circle_radius))







if __name__ == '__main__':
    main()