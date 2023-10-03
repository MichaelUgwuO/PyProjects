# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    calc.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: mugwu <mugwu@student.42.fr>                +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/09/28 14:30:34 by mugwu             #+#    #+#              #
#    Updated: 2023/10/03 17:44:36 by mugwu            ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

#Making a simple calculator

First_num = int(input("First number: "))
Operand = input("input operation: ")
Var_operand = ["+", "-", "/", "*"]
Second_num = int(input("Second number: "))

if not (-9223372036854775807 <= First_num <= 9223372036854775807) or not (-9223372036854775807 <= Second_num <= 9223372036854775807):
    print("Syntax Error")

if Operand == "+":
    Solution = (First_num + Second_num)
    print("Your answer is: ", Solution)
elif Operand == "-":
    Solution = (First_num - Second_num)
    print("Your answer is:", Solution)
elif Operand == "*":
    Solution = (First_num * Second_num)
    print("Your answer is:", Solution)
elif Operand == "/" and Second_num != 0:
    Solution = (First_num / Second_num)
    print("Your answer is:", Solution)
elif Operand == "/" and Second_num == 0:
    print("Math Error")
else:
    print("Syntax Error")