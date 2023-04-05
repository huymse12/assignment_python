import numpy as np
import matplotlib.pyplot as plt

import db
import repository
import services
import pandas as pd
import seaborn as sb

mysql_db = db.connect_my_sql()
laptop_repository = repository.LaptopBestSellerRepository(mysql_db)


def visualize_bar_chart_avg_median(df):
    bar_width = 0.25
    fig = plt.subplots(figsize=(12, 8))

    br1_median = np.arange(len(df["MedianOldPrice"]))
    br2_median = np.arange(len(df["MedianNewPrice"]))
    br1_mean = [x + bar_width for x in br1_median]
    br2_mean = [x + bar_width for x in br1_median]

    plt.bar(br1_median, df["MedianOldPrice"], color='r', width=bar_width,
            edgecolor='grey', label='MedianOldPrice')
    plt.bar(br2_median, df["MedianNewPrice"], color='g', width=bar_width,
            edgecolor='grey', label='MedianNewPrice')
    plt.bar(br1_mean, df["MeanOldPrice"], color='b', width=bar_width,
            edgecolor='grey', label='MeanOldPrice')
    plt.bar(br2_mean, df["MeanNewPrice"], color='y', width=bar_width,
            edgecolor='grey', label='MeanNewPrice')

    # Adding Xticks
    plt.xlabel('Brand', fontweight='bold', fontsize=15)
    plt.ylabel('Price', fontweight='bold', fontsize=15)
    plt.xticks([r + bar_width for r in range(len(df["MedianOldPrice"]))],
               df["Brand"])

    plt.legend()
    plt.show()


def visualize_bar_chart_count(df):
    bar_width = 0.25
    fig = plt.subplots(figsize=(12, 8))

    br1_median = np.arange(len(df["Count"]))

    plt.bar(br1_median, df["Count"], color='r', width=bar_width,
            edgecolor='grey', label='Count')

    # Adding Xticks
    plt.xlabel('Brand', fontweight='bold', fontsize=15)
    plt.ylabel('Total', fontweight='bold', fontsize=15)
    plt.xticks([r + bar_width for r in range(len(df["Count"]))],
               df["Brand"])

    plt.legend()
    plt.show()


def visualize_bar_chart_min_max(df):
    bar_width = 0.25
    fig = plt.subplots(figsize=(12, 8))

    br1_min = np.arange(len(df["MinPercentDiscount"]))
    br1_max = [x + bar_width for x in br1_min]

    plt.bar(br1_min, df["MinPercentDiscount"], color='r', width=bar_width,
            edgecolor='grey', label='MinPercentDiscount')
    plt.bar(br1_max, df["MaxPercentDiscount"], color='g', width=bar_width,
            edgecolor='grey', label='MaxPercentDiscount')

    # Adding Xticks
    plt.xlabel('Brand', fontweight='bold', fontsize=15)
    plt.ylabel('PercentDiscount', fontweight='bold', fontsize=15)
    plt.xticks([r + bar_width for r in range(len(df["MinPercentDiscount"]))],
               df["Brand"])

    plt.legend()
    plt.show()


def visualize_scatter_plot_new_price(df):
    sb.set_theme(style="whitegrid", palette="muted")

    # Draw a categorical scatterplot to show each observation
    ax = sb.swarmplot(data=df, x="NewPrice", y="Brand")
    ax.set(ylabel="")
    plt.show()
    pass


def visualize_median_avg():
    df = init_data_frame_avg_median()
    visualize_bar_chart_avg_median(df)


def visualize_count():
    df = init_data_frame_count()
    visualize_bar_chart_count(df)


def visualize_min_max():
    df = init_data_frame_min_max_percent_discount()
    visualize_bar_chart_min_max(df)


def visualize_best_seller_new_price():
    df = init_data_frame_new_price_best_seller()
    print(df)
    visualize_scatter_plot_new_price(df)


def init_data_frame_avg_median():
    df = init_data_frame(["Brand", "OldPrice", "NewPrice"])
    df_median = df.groupby(['Brand']).median().reset_index() \
        .rename(columns={
        'OldPrice': "MedianOldPrice",
        "NewPrice": "MedianNewPrice"
    })
    df_average = df.groupby(['Brand']).mean().reset_index() \
        .rename(columns={
        'OldPrice': "MeanOldPrice",
        "NewPrice": "MeanNewPrice"
    })
    df = df_median.merge(df_average, on='Brand')
    return df


def init_data_frame_count():
    df = init_data_frame(["Brand", "OldPrice", "NewPrice"])
    df_count = df.groupby(['Brand'])['Brand'].count().reset_index(name='Count')
    return df_count


def init_data_frame_min_max_percent_discount():
    df = init_data_frame(['Brand', 'PercentDiscount'])
    df_min = df.groupby(['Brand']).min().reset_index().rename(columns={
        "PercentDiscount": "MinPercentDiscount"
    })
    df_max = df.groupby(['Brand']).max().reset_index().rename(columns={
        "PercentDiscount": "MaxPercentDiscount"
    })
    df = df_min.merge(df_max, on='Brand')
    return df


def init_data_frame_new_price_best_seller():
    df = init_data_frame_best_seller(['Brand', 'NewPrice'])
    return df


def init_data_frame(fields):
    data_laptop = laptop_repository.get_laptop_for_statistic(fields)
    data_arr = []
    for item in data_laptop:
        data_arr.append(item)
    df = pd.DataFrame(data_arr, columns=fields)
    return df


def init_data_frame_best_seller(fields):
    data_laptop = laptop_repository.get_best_seller_laptop_for_statistic(fields)
    data_arr = []
    for item in data_laptop:
        data_arr.append(item)
    df = pd.DataFrame(data_arr, columns=fields)
    return df


# visualize_median_avg()
# visualize_count()
# visualize_min_max()
visualize_best_seller_new_price()
