class Solution:
    def flipAndInvertImage(image):
        for row in image:
        # Reverse the row
            row.reverse()
            # Invert the values in the row
            for j in range(len(row)):
                row[j] = 1 - row[j]
    
        return image
        