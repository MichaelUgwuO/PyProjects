# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    matplot.py                                         :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: mugwu <mugwu@student.42.fr>                +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/09/29 20:44:56 by mugwu             #+#    #+#              #
#    Updated: 2023/10/01 07:58:35 by mugwu            ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

x = [5, 8, 12, 17, 25]
y = [30, 24, 17, 11, 5]

plt.plot(x, y)
plt.xlabel('Supply')
plt.ylabel('Demand')
plt.title('Supply and demand graph')
plt.show()