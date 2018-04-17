import matplotlib.image as mpimg
import numpy as np

bg = mpimg.imread("bg.png")
pattern = mpimg.imread("pattern_2.png")

pattern_alpha = np.empty([len(pattern), len(pattern[0]), 4])

for i in range(0, len(pattern)):
    for j in range(0, len(pattern[i])):
        pixel = pattern[i][j]
        pattern_alpha[i][j] = [1, 1, 1, 1 - pixel[0]]

"""CENTER"""
startX = int(len(bg) / 2 - len(pattern_alpha) / 2)
startY = int(len(bg[0]) / 2 - len(pattern_alpha[0]) / 2)
endX = startX + len(pattern_alpha)
endY = startY + len(pattern_alpha[0])

result = np.empty([len(bg), len(bg[0]), 3])

for i in range(0, len(bg)):
    for j in range(0, len(bg[0])):
        if startX <= i < endX and startY <= j < endY:
            aX = i - startX
            aY = j - startY
            aPixel = pattern_alpha[aX][aY]
            if aPixel[3] > 0:
                result[i][j] = [1, 1, 1]
            else:
                pixel = bg[i][j]
                result[i][j] = [pixel[0], pixel[1], pixel[2]]
        else:
            pixel = bg[i][j]
            result[i][j] = [pixel[0], pixel[1], pixel[2]]

mpimg.imsave("result.png", result)