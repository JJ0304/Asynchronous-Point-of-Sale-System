import asyncio
import random


class Inventory:
    def __init__(self):
        self.catalogue = {
            "Burgers": [
                {"id": 1, "name": "Python Burger", "price": 5.99},
                {"id": 2, "name": "C Burger", "price": 4.99},
                {"id": 3, "name": "Ruby Burger", "price": 6.49},
                {"id": 4, "name": "Go Burger", "price": 5.99},
                {"id": 5, "name": "C++ Burger", "price": 7.99},
                {"id": 6, "name": "Java Burger", "price": 7.99}
            ],
            "Sides": {
                "Fries": [
                    {"id": 7, "size": "Small", "price": 2.49}, 
                    {"id": 8, "size": "Medium", "price": 3.49}, 
                    {"id": 9, "size": "Large", "price": 4.29}
                ],
                "Caesar Salad": [
                    {"id": 10, "size": "Small", "price": 3.49}, 
                    {"id": 11, "size": "Large", "price": 4.49}
                ]
            },