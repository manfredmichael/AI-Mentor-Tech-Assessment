

<div align="center">
<img src="https://scontent.fcgk42-1.fna.fbcdn.net/v/t39.30808-1/327178808_710452637414345_956158677198095703_n.png?stp=dst-png_p120x120&_nc_cat=110&ccb=1-7&_nc_sid=4da83f&_nc_ohc=WwFbJYYHLy8AX-WiVM7&_nc_ht=scontent.fcgk42-1.fna&oh=00_AfDWUTAd61a2aqNbW4jkge86mdX40bxJXmfoqJrT896fSQ&oe=65EAB7EC" alt="drawing" width="200"/>
  
<br/>
<br/>
<br/>

# TerraStore
Technical Assessment for Mentor Data Science & AI
</div>

### Website Interface

You can try the Streamlit Interface here: https://ai-mentor-tech-assessment-jfgowl3jho9m3lxnxavemo.streamlit.app/

#### How to use?

There are 2 pages. You could choose them on the sidebar.

1. Recommendation System

In this page, you could see which products are recommended for a given user.

2. Cashback & Discount.

In this page, you could see which users are more likely to buy a given products, hence you might want to encourage those users with discounts.


Note that you can change the prices or even move the product into different categories to see how the users react.

### Data Preparation & Model Training

* Data Preparation: https://github.com/manfredmichael/AI-Mentor-Tech-Assessment/blob/main/model-training/dataset_creation.ipynb
* Model Training: https://github.com/manfredmichael/AI-Mentor-Tech-Assessment/blob/main/model-training/training.ipynb

For this solution, I used Google's Wide and Deep Model as inspiration. I created the model from scratch with Tensorflow and Monitored the training process with WandB.

WandB Report: https://wandb.ai/nodeflux-internship/tech-assessment-recsyc/reports/TerraStore-Recommendation-System-with-Wide-Deep-Architecture--Vmlldzo3MDE1OTE1

### Author's Note

This project is far from perfect. There were a lot of steps skipped to save time. It is not supposed to be taken as real solution into recommendation system problem instead as a learning material.

<br/>
<hr>

Reference: https://blog.research.google/2016/06/wide-deep-learning-better-together-with.html

