import pandas as pd
import numpy as np
import matplotlib


def division():
    x = input("gimme a number:")
    y = input("gimme gimme gimme a number after midnight:")

    try:
        x = int(x)
        y = int(y)
        print(x/y)

    except ZeroDivisionError:
        print("uh uh uuuuuh")

    except ValueError:
        print("sei mal realistisch!")

division()
