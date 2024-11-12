#File: subplots.py
import numpy as np
import matplotlib.pyplot as plt

def side_by_side(x):
    #will create side by side subplots of cosine an sine graphs
    y1 = np.cos(x)
    y2 = np.sin(x)
    fig, ax = plt.subplots(1, 2, figsize = (20, 5))
    ax[0].plot(x, y1)
    ax[1].plot(x, y2)
    ax[0].set_title(f"h(x) = cos(x)")
    ax[1].set_title(f"k(x) = sin(x)")
    ax[0].set_ylim(-2, 2)
    ax[1].set_ylim(-2, 2)
    
    ax[0].set_xlabel("x")
    ax[0].set_ylabel("y")
    
    ax[1].set_xlabel("x")
    ax[1].set_ylabel("y")
    plt.show()

def on_top(x):
    # will create top down subplots of cosine an sine
    y1 = np.cos(x)
    y2 = np.sin(x)
    fig, ax = plt.subplots(2, 1, figsize = (10, 20))
    ax[0].plot(x, y1)
    ax[1].plot(x, y2)
    ax[0].set_title(f"h(x) = cos(x)")
    ax[1].set_title(f"k(x) = sin(x)")
    ax[0].set_ylim(-2, 2)
    ax[1].set_ylim(-2, 2)
    
    ax[0].set_xlabel("x")
    ax[0].set_ylabel("y")
    
    ax[1].set_xlabel("x")
    ax[1].set_ylabel("y")
    plt.show()
