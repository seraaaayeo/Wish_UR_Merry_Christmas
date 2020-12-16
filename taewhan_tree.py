import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


def make_tree(tree_height=100, tree_width=50, quality=20, slope=1.5, leaf_height=0.8, trunk_width=0.05, orna_freq=1,
              bark_color='#660000', bg_color='#FFFFFF', orna1_color='#FFFF00', orna2_color='#FF0000',
              leaf_color='#003300'):
    tree = np.arange(tree_height * tree_width).reshape(tree_height, tree_width).astype('float64')
    tree[(tree % tree_width > tree_width // 2 + tree // (tree_height * slope)) |
         (tree % tree_width < tree_width // 2 - tree // (tree_height * slope))] = 0
    tree[(tree >= tree_height * tree_width * leaf_height) &
         ((tree % tree_width > tree_width // 2 + tree_width * trunk_width) |
          (tree % tree_width < tree_width // 2 - tree_width * trunk_width))] = 0
    tree[tree > 0] = 1
    tree[:int(tree_height * leaf_height), :] *= np.random.normal(40, orna_freq * 4,
                                                                 (int(tree_height * leaf_height), tree_width))
    tree[int(tree_height * leaf_height):, :] *= -20

    palette = [bark_color, bg_color, orna1_color, leaf_color, orna2_color]
    cmap = sns.color_palette(palette, len(palette), as_cmap=True)

    fig, ax = plt.subplots(1, 1, figsize=(tree_width // quality, tree_height // quality))
    sns.heatmap(tree - 20, center=0, cmap=cmap, vmin=-50, vmax=50, cbar=False, xticklabels=False, yticklabels=False)
    plt.show()


if '__name__' == '__main__':
    make_tree(tree_height=200, tree_width=100, quality=25, slope=1.7, leaf_height=0.85, trunk_width=0.1, orna_freq=1.2,
              bark_color='#663333', bg_color='#EEEEFF', leaf_color='#336633')
