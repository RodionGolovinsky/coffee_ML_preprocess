import os
import matplotlib.pyplot as plt
import pandas as pd

materials = ['au', 'ni', 'cu', 'gc']
au, ni, cu, gc = [], [], [], []
au_names, ni_names, cu_names, gc_names = [], [], [], []
for root, dirs, files in os.walk('correct_data'):
    for file in files:
        if file.endswith('.csv'):
            if 'ni' in file:
                df = pd.read_csv(os.path.join(root, file))
                ni.append(df)
                ni_names.append(file)
            if 'au' in file:
                df = pd.read_csv(os.path.join(root, file))
                au.append(pd.read_csv(os.path.join(root, file)))
                au_names.append(file)
            if 'gc' in file:
                df = pd.read_csv(os.path.join(root, file))
                gc.append(pd.read_csv(os.path.join(root, file)))
                gc_names.append(file)
            if 'cu' in file:
                df = pd.read_csv(os.path.join(root, file))
                cu.append(pd.read_csv(os.path.join(root, file)))
                cu_names.append(file)
# for m in materials:
#     for i, df in enumerate(locals()[m]):
#         print(i)
#         x = df['Time']
#         y = df['Current']
#         fig, axs = plt.subplots(nrows=4, ncols=5)
#         fig.suptitle(f'{m}__graph')
#         row = i % 4
#         col = i // 4
#         axs[row, col].plot(x, y)
#         name = m + '_names'
#         axs[row, col].set_title(locals()[name][i])
#         # plt.imshow(fig)
#     plt.show()
#     fig.savefig(f'correct_data/graphs/{m}.png')
#
#     #
#     break
for m in materials:
    for i, df in enumerate(locals()[m]):
        x = df['Time']
        y = df['Current']
        plt.grid()
        plt.plot(x, y)
        name = m + '_names'
        plt.title(locals()[name][i])
        plt.show()
        plt.savefig(f'correct_data/graphs/{locals()[name][i]}.png')
        plt.close()
