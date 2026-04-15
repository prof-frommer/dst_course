import marimo

__generated_with = "0.23.0"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo

    return (mo,)


@app.cell
def _(mo):
    mo
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    # hello world
    """)
    return


@app.cell
def _():
    3+9
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Slider example
    """)
    return


@app.cell
def _(mo):
    xx = mo.ui.slider(0, 10, value=2, label="Choose a number", show_value=True)
    xx
    return (xx,)


@app.function
def square(n):
    return n**2


@app.cell
def _(xx):
    square(xx.value)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Dataframe example
    """)
    return


@app.cell
def _():
    import pandas as pd
    df0 = pd.read_csv('calc1.csv')
    return df0, pd


@app.cell
def _(df0):
    df0
    return


@app.cell
def _(mo):
    col = mo.ui.dropdown(options=["exam1", "exam2", "overall"], label="Column")
    threshold = mo.ui.slider(0, 1, step=.1,value=0.70, label="Minimum score")
    col, threshold
    return col, threshold


@app.cell
def _(col, filtered, threshold):
    import matplotlib.pyplot as plt

    plt.hist(filtered[col.value], bins=5)
    plt.title(f"{col.value} (≥ {threshold.value})")
    plt.show()
    return (plt,)


@app.cell
def _(col, df0, threshold):
    filtered = df0[df0[col.value] >= threshold.value]
    filtered
    return (filtered,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Another dataframe
    """)
    return


@app.cell
def _(pd):
    df = pd.read_csv('trans-atlantic1599.csv')
    df
    return (df,)


@app.cell
def _(df):
    df.columns
    return


@app.cell
def _(df, mo):
    cols = mo.ui.dropdown(options=df.columns, label="Category")
    cols
    return (cols,)


@app.cell
def _(col, cols, df, plt):

    counts = df[cols.value].value_counts()

    plt.figure()
    counts.plot(kind="bar")
    plt.title(f"Counts of {col.value}")
    plt.ylabel("Count")
    plt.show()
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
