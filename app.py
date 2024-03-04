import time
import streamlit as st

import pandas as pd 
from pipeline import get_recommendation

purchase_history = pd.read_csv('model-training/purchase_history.csv')
customer_interactions = pd.read_csv('model-training/customer_interactions.csv')
product_details = pd.read_csv('model-training/product_details.csv')

data = purchase_history.merge(customer_interactions)
data = data.merge(product_details)

n_products = data.product_id.nunique()
n_users = data.user_id.nunique()
n_category =  data.category_id.nunique()

unique_products = list(data.product_id.unique())
unique_users = list(data.user_id.unique())
unique_category = list(data.category_id.unique())

def recommendation_system():

    user_id = st.selectbox(
        "Which user id would you want to see?",
        unique_users,
        index=None,
        placeholder="Select user id",
    )

    # Session details
    page_views = st.number_input('Insert a page views (click amount)', min_value=0, step=1)

    session_time = st.number_input('Insert a session time in seconds', min_value=0, step=1)

    if user_id is not None:
        recommendations = get_recommendation(
            user_id=user_id, 
            page_views=page_views, 
            session_time=session_time
        )
        recommendations['category_id'] = recommendations['category_id'].astype(str)

        st.write("#### Top 10 products for user {}".format(user_id))
        st.dataframe(
            recommendations.head(10),
            hide_index=True,
            column_config={
            "product_id": st.column_config.NumberColumn(
                "Product ID",
                format="%d",
            )
        },)

        st.write("#### Top 10 categories for user {}".format(user_id))
        st.dataframe(
            pd.Series(recommendations.category_id.unique()[:10], name='Category ID'),
            hide_index=True)
        


def main():
    page_names_to_funcs = {
        # "From Uploaded Picture": from_picture,
        "Recommendation system": recommendation_system
    }

    selected_page = st.sidebar.selectbox("Select a page", page_names_to_funcs.keys())
    page_names_to_funcs[selected_page]()

if __name__ == "__main__":
    st.set_page_config(
        page_title="Recommendation  System - Technical Interview", page_icon=":pencil2:"
    )
    st.title("Recommendation  System")
    # st.sidebar.subheader("Configuration")
    main()