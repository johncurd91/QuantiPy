from PIL import Image
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# Load control image
img_control = Image.open("images/control_image.png")
np_array_control = np.array(img_control.getdata())
df_control = pd.DataFrame(np_array_control, columns=["R", "G", "B", "a"])

# Load test image
img_test = Image.open("images/test_image.png")
np_array_test = np.array(img_test.getdata())
df_test = pd.DataFrame(np_array_test, columns=["R", "G", "B", "a"])

# Tidy and combine dataframes

df_control = pd.melt(
    frame=df_control,
    value_vars=["R", "G", "B", "a"],
    value_name="Signal",
    var_name="Channel"
)

df_test = pd.melt(
    frame=df_test,
    value_vars=["R", "G", "B", "a"],
    value_name="Signal",
    var_name="Channel"
)


df = pd.concat([df_control, df_test], keys=["Control", "Test"])
df = df.rename_axis(["Condition", "Pixel"]).reset_index()

# Set threshold and remove outliers and irrelevant data
threshold = 100
df = df[df["Signal"] >= 100]
df = df[df["Channel"] != "G"]
df = df[df["Channel"] != "a"]

# Plot
sns.set_context("notebook")
sns.set_style("darkgrid")

sns.barplot(
    data=df,
    y="Signal",
    x="Channel",
    hue="Condition",
    capsize=0.1
)
plt.title("Quantipy plot")
plt.show()

















