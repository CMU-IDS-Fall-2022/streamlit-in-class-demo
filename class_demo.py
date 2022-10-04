import streamlit as st
import pandas as pd
import altair as alt

st.header("Our First Application")
st.write("Hello World!")

@st.cache
def load(url):
    return pd.read_json(url)

df = load("https://cdn.jsdelivr.net/npm/vega-datasets@2/data/penguins.json")

if st.checkbox("Show Raw Data"):
    st.write(df)

#picked = alt.selection_single(on="mouseover", empty="none")
#picked = alt.selection_multi()
#picked = alt.selection_interval(encodings=["x"])
#picked = alt.selection_single(on="mouseover", fields=["Species", "Island"])

# input_dropdown = alt.binding_select(options=["Adelie", "Chinstrap", "Gentoo"], name="Select a Species: ")
# picked = alt.selection_single(encodings=["color"], bind=input_dropdown)


# scatter = alt.Chart(df).mark_point().encode(
#     alt.X("Flipper Length (mm)", scale=alt.Scale(zero=False)),
#     alt.Y("Body Mass (g)", scale=alt.Scale(zero=False)),
#     color = alt.condition(picked, "Species", alt.value("lightgrey"))
# ).add_selection(picked)

# st.write(scatter)

brush = alt.selection_interval(encodings=["x"])

scatter = alt.Chart(df).mark_point().encode(
    alt.X("Flipper Length (mm)", scale=alt.Scale(zero=False)),
    alt.Y("Body Mass (g)", scale=alt.Scale(zero=False)),
    alt.Color("Species")
).add_selection(brush)

hist = alt.Chart(df).mark_bar().encode(
    alt.X("Body Mass (g)", bin=True),
    alt.Y("count()"),
    alt.Color("Species")
).transform_filter(brush)

st.write(scatter & hist)


#scales = alt.selection_interval(bind="scales")
#st.write(scatter.add_selection(scales))



# min_weight = st.slider("Minimum Body Mass", 2500, 6500)
# st.write(min_weight)

# scatter_filtered = scatter.transform_filter(f"datum['Body Mass (g)'] >= {min_weight}")
# st.write(scatter_filtered)