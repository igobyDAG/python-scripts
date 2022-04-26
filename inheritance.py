class Paint:

    def __init__(self, buckets, color):  # Or get house area and height
        self.color = color
        self.buckets = buckets

    def total_price(self):
        if self.color == "white":
            return self.buckets * 1.99
        else:
            return self.buckets * 2.19


class DiscountedPaint(Paint):
    def discounted_price(self, discount_percentage):
        return self.total_price() - self.total_price() * discount_percentage
