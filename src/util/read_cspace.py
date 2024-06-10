from PIL import Image, ImageOps
import numpy as np
from numpy import ndarray
import matplotlib.pyplot as plt


# TODO fix the img creation - address artifacts
def create_img() -> None:
    img = Image.open("../resources/c_space.png")
    img = ImageOps.grayscale(img)

    # Invert grayscale np array
    np_img = ~np.array(img)
    np_img[np_img > 0] = 1

    plt.set_cmap("binary")
    # plt.imshow(np_img)

    # Save image as a .npy
    np.save("../resources/c_space.npy", np_img)


def read_img() -> None:
    grid = np.load("../resources/c_space.npy")
    plt.imshow(grid)
    plt.tight_layout()
    plt.show()


def read_to_np_array() -> ndarray:
    return np.load("../resources/c_space.npy")


create_img()
read_img()
