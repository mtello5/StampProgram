"""
start
get the numbers of sheets
sheets / 5
round answer to next number
output the result to the user
end
"""
import math
#input: sheet
def calculate(sheet):
    answer = sheet / 5
    rounded = round(answer)
    print("sheet is : ", answer)
    print("The answer is: ", rounded)
    print("rounded is: ", rounded)
    print("================================")
    # output: number of stamps for sheets
    return rounded

output = calculate(10000)
print("the number of stamps needed is: ", output)

