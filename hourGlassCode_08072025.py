"""
[
[1 1 1 1 1 1]
[1 1 1 1 1 1]
[1 1 1 1 1 1]
[1 1 1 1 1 1]
[1 1 1 1 1 1]
[1 1 1 1 1 1]
]

Sample Hourglass:
1 1 1
  1
1 1 1
"""



def hourglassSum(arr):
    hourglass_max_sum = -82 # initiating this to -82 as (-9*9 = -81) -81 is the maximum we can get
    temp_var = -81
    # finding the row length
    arr_row = len(arr)

    # finding the column length
    arr_col = len(arr[0])

    # print("arr_row: ", arr_row)
    # print("arr_col: ", arr_col)

    # this if is to check the row and column length of the given matrix
    # constraint # 2
    if (arr_row <= -1 or arr_col <= -1 or arr_row > 6 or arr_col > 6):
        return -1 # -1 is returned to indicate that the input is having issues
    # print("range(arr_row - 2): ", range(arr_row - 2))
    # print("range(arr_col - 2: ", range(arr_col - 2))
    for i in range(arr_row - 2): # range (0,4,1) -> starting from 0, ending at 3 (4-1) and hop with 1
        for j in range(arr_col - 2):
            # print("********************")
            # print(arr[i][j]     , " ", arr[i][j+1]  , " ", arr[i][j+2]  )
            # print(arr[i+1][j]   , " ", arr[i+1][j+1], " ", arr[i+1][j+2])
            # print(arr[i+2][j]   , " ", arr[i+2][j+1], " ", arr[i+2][j+2])
            # print("********************")
            # print("********************")
            temp_var = (arr[i][j] + arr[i][j+1] + arr[i][j+2] + arr[i+1][j] + arr[i+1][j+1] + arr[i+1][j+1] + arr[i+2][j] + arr[i+2][j+1] + arr[i+2][j+2])
            # Constraint # 2 (-9 <= i, j <= 9)
            if (temp_var > 81 or temp_var < -81):
                return -1 # 81 or -81 is the max and min values we can get from 3*3 matrix which has all 9 or -9
            hourglass_sum = (arr[i][j] + arr[i][j+1] + arr[i][j+2] + arr[i+1][j+1] + arr[i+2][j] + arr[i+2][j+1] + arr[i+2][j+2])
            #print("hourglass_sum", hourglass_sum)
            hourglass_max_sum = max(hourglass_max_sum, hourglass_sum)

    return hourglass_max_sum

# Example Usage:
matrix = [
    [-1, -1,  0, -9, -2, -2],
    [-2, -1, -6, -8, -2, -5],
    [-1, -1, -1, -2, -3, -4],
    [-1, -9, -2, -4, -4, -5],
    [-7, -3, -3, -2, -9, -9],
    [-1, -3, -1, -2, -4, -5]
]

result = hourglassSum(matrix)
print(f"The maximum hourglass sum is: {result}")


