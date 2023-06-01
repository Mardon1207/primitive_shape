class Polygon:
    def __init__(self, height, width) -> None:
        self.height = height
        self.width = width

    def getArea(self):
        """
        This method finds the area of the Polygon.

        Args:
            No
        Returns:
            float or int: return perimeter of the polygon.
        """
        a=self.height
        b=self.width
        s=a*b
        return s

    def getPerimeter(self):
        """
        This method finds the perimeter of the Polygon.

        Args:
            No
        Returns:
            float or int: return perimeter of the polygon.
        """
        a=self.height
        b=self.width
        p=2*(a+b)
        return p